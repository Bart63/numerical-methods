from os import listdir
from os.path import isfile, join
import validator as valid
import numpy as np
import sys

class Matrix():
    folderPath = ".\\matrices"

    def __init__(self):
        self.files = []
        self.clearVars()

    def clearVars(self):
        self.epsilon = -1
        self.accuracy = sys.maxsize
        self.iterations = sys.maxsize
        self.currentIter = 0
        self.matrix=[]
        self.X = np.array([])
        self.B = np.array([])
        self.D = np.array([])
        self.A = np.array([])
        self.err = []

    def setEpsilon(self, e):
        self.epsilon=e

    def setIterations(self, i):
        self.iterations=i

    def searchFiles(self):
        self.files = [f for f in listdir(self.folderPath)
                         if isfile(join(self.folderPath, f))
                         if f.endswith('.txt')]

    def getFiles(self) -> list():
        self.searchFiles()
        return self.files

    def getAllMat(self):
        return (self.A, self.B, self.X)

    def isDiagonallyDominant(self) -> bool:
        D = np.abs(self.D)
        S = np.sum(np.abs(self.A), axis=1) - D
        if np.all(D >= S):
            return True
        return False

    def loadMatrix(self, index):
        self.clearVars()
        filePath = self.folderPath+"\\"+self.files[index]
        matrixFile = open(filePath, "r")
        for line in matrixFile:
            temp = []
            for item in line.split():
                if not valid.isFloat(item):
                    return False
                temp.append(float(item))
            self.matrix.append(temp)
        matrixFile.close()
        if not self.loadMatrices():
            return False

    def loadMatrices(self):
        rows = len(self.matrix)
        for row in self.matrix:
            temp=[]
            if len(row)>=rows:
                for j in range(rows):
                    temp.append(row[j])
                if len(self.A)==0:
                    self.A = np.append(self.A, temp, axis=0)
                else:
                    self.A  = np.vstack((self.A, temp))
            else:
                return False
            if len(row)>=rows+1:
                self.B = np.append(self.B, row[rows])
            else:
                self.B = np.append(self.B, 0)
            if len(row)>=rows+2:
                self.X = np.append(self.X, row[rows+1])
            else:
                self.X = np.append(self.X, 0)
        self.D = np.diagonal(self.A)
        return True

    def satisfiedCriteria(self) -> bool:
        accuracy = self.accuracy > self.epsilon
        iterations = self.currentIter < self.iterations
        return not (accuracy and iterations)

    def getStats(self):
        return (self.currentIter, self.accuracy)

    def getX(self):
        return self.X

    def getErr(self):
        return self.err

    def calcAcc(self, delta):
        i=0
        temp=[]
        while i < len(self.X):
            temp.append(abs(delta[i]/self.X[i]) if self.X[i]!=0 else 0)
            i+=1
        self.accuracy = max(temp)
        self.err.append(self.accuracy)

    def calc(self):
        while not self.satisfiedCriteria():
            delta = np.power(self.D,-1) * (self.B - np.dot(self.A, self.X))
            self.X += delta
            self.calcAcc(delta)
            self.currentIter +=1

if __name__=="__main__":
    ml = Matrix()
    ml.searchFiles()
    for i, f in enumerate(ml.getFiles()):
        print(f"{i+1}. {f}")
    ml.loadMatrix(0)