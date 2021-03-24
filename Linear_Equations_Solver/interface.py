import matrix as mx
import validator as valid
from sys import float_info
from plot import plot

class Interface():
    def __init__(self):
        self.matrices = mx.Matrix()
        self.criteria = ["Ilosc iteracji", "Dokladnosc"]
        self.start()

    def start(self):
        self.chooseMatrix()
        self.showAllMat()
        self.chooseCriteria()
        self.calc()
        self.showStats()
        self.showX()
        self.showPlot()

    def chooseMatrix(self):
        files = self.matrices.getFiles()
        if len(files) == 0:
            print("Brak plikow txt")
            raise Exception("Empty folder")
        index = 1
        if len(files) > 1:
            print("Wybierz plik")
            index = self.showAndChoose(files)
            if not valid.isDigit(index, len(files)):
                self.chooseMatrix()
                return
        index = int(index)
        good = self.matrices.loadMatrix(index-1)
        if good==False:
            print("Blad, sprobu ponownie")
            self.chooseMatrix()
            return
        if not self.matrices.isDiagonallyDominant():
            print("Macierz nie ma dominujacej przekatnej")
            self.chooseMatrix()
            return

    def calc(self):
        self.matrices.calc()

    def showX(self):
        X = self.matrices.getX()
        for i,x in enumerate(X):
            print(f"x{i+1} = {x}")

    def showAllMat(self):
        print()
        mats = self.matrices.getAllMat()
        print("Macierz A:")
        for row in mats[0]:
            print(row)
        print()
        print("Nacierz B:")
        print(mats[1])
        print()
        print("Macierz X:")
        print(mats[2])
        print()

    def showStats(self):
        stats = self.matrices.getStats()
        print(f"Liczba iteracji: {stats[0]}")
        print(f"Dokladnosc: {stats[1]}")

    def showPlot(self):
        plot(self.matrices.getErr())

    def chooseCriteria(self):
        print("Wybierz kryterium")
        index = self.showAndChoose(self.criteria)
        if not valid.isDigit(index, len(self.criteria)):
            self.chooseCriteria()
            return
        index = int(index)
        if index==1:
            self.setIterations()
        else:
            self.setEpsilon()

    def setEpsilon(self):
        epsilon = input("Podaj epsilon: ")
        if not valid.isFloat(epsilon):
            self.setEpsilon()
            return
        elif float(epsilon)<=0:
            print("Epsilon musi byc wiekszy od 0")
            self.setEpsilon()
            return
        epsilon=float(epsilon)
        self.matrices.setEpsilon(epsilon)

    def setIterations(self):
        iterations = input("Podaj liczbę iteracji: ")
        if not valid.isDigit(iterations, float_info.max):
            self.setIterations()
            return
        iterations = int(iterations)
        self.matrices.setIterations(iterations)

    def showAndChoose(self, arr) -> str:
        for index, name in enumerate(arr):
            print(f"{index+1}. {name}")
        return input("Index: ")

if __name__=="__main__":
    interface = Interface()