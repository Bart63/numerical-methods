import numpy as np
from math import pi
import variables as df
from plot import plot

class Methods():
    def __init__(self):
        self.resetVars()

    def resetVars(self):
        self.what=0

    def getEquation(self) -> str:
        return df._functions_[self.chosenFunction]["string"]

    def setVars(self, kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def getVal(self, x) -> float:
        return df._functions_[self.chosenFunction]["calc"](x)

    def calcPoints(self):
        self.points = np.array([0.5*(self.a+self.b) +
                       0.5*(self.b-self.a)*np.cos((2*i+1)*pi/(2*self.nofpoints))
                       for i in range(0, self.nofpoints)])
        self.points = self.points[::-1]
        self.pointsy = df._functions_[self.chosenFunction]["calc"](self.points)
        self.w = [1/np.prod(xi-np.delete(self.points, i))
                  for i,xi in enumerate(self.points)]

    def startCalc(self):
        self.X = np.linspace(self.a,self.b,int(self.b-self.a)*30)
        self.calcPoints()
        self.baricentric()
        self.newton()

        plot((self.X, df._functions_[self.chosenFunction]["calc"](self.X)),
            (self.X, self.Y_bar), (self.X, self.Y_new), (self.points, self.pointsy),
             df._functions_[self.chosenFunction]["string"])

    def baricentric(self):
        self.Y_bar=[]
        for x in np.nditer(self.X):
            L=self.w/(x-self.points)
            self.Y_bar.append(self.pointsy@L/sum(L))

    def calcNewtonCoefs(self):
        n = len(self.pointsy)
        coef = np.zeros([n,n])
        coef[:,0] = self.pointsy
        for j in range(1, n):
            for i in range(n-j):
                # f(xi,xj) = (yj-yi)/(xj-xi)
                coef[i][j] = (coef[i+1][j-1]-coef[i][j-1])/(self.points[i+j]-self.points[i])
        self.coef=coef[0, :]

    def calcNewtonPoly(self):
        n=len(self.points)-1
        p=self.coef[n]

        for k in range(1,n+1):
            p=self.coef[n-k]+(self.X-self.points[n-k])*p
        self.Y_new=p

    def newton(self):
        self.calcNewtonCoefs()
        self.calcNewtonPoly()