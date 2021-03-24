import variables as df
from numpy import linspace
from math import ceil
import sys

class Methods():
    def __init__(self):
        self.epsilon = -1
        self.iterations = sys.maxsize
        self.resetVars()

    def resetVars(self):
        self.iters = 0
        self.x1 = 0
        self.x2 = 0
        self.x3 = sys.float_info.max
        self.y = 0
        self.cycle = 0.000000000001

    def getEquation(self) -> str:
        return df._functions_[self.chosenFunction]["string"]

    def exampleRoots(self) -> str:
        return df._functions_[self.chosenFunction]["roots"]

    def setVars(self, kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def getVal(self, x) -> float:
        return df._functions_[self.chosenFunction]["calc"](x)

    def getVal_d(self, x) -> float:
        return df._functions_[self.chosenFunction]["calc_d"](x)

    def calcXY(self, nOfPoints, start=False, end=False) -> tuple:
        if type(start)!=bool and type(end)!=bool:
            calc_nOfPoints = (end-start)
            if start>self.a:
                calc_nOfPoints /= (end-self.a)
            else:
                calc_nOfPoints /= (self.b-start)
            calc_nOfPoints *= nOfPoints
            calc_nOfPoints = ceil(calc_nOfPoints)
            X = linspace(start, end, calc_nOfPoints)
        else:
            X = linspace(self.a, self.b, nOfPoints)
        Y = self.getVal(X)
        return (X,Y)

    def calc_all(self):
        print("Bisekcja")
        res_b = self.start_bisection()
        if type(res_b)!=bool:
            self.getAccuracy()
        print("")
        print("Newton")
        res_n = self.start_newton()
        if type(res_n)!=bool:
            self.getAccuracy()
        return (res_b, res_n)

    def initCrtArr(self):
        if(self.chosenMethod==0):
            self.critArr = {"x1": self.x1, "x2": self.x2, "e": self.epsilon}
        elif(self.chosenMethod==1):
            self.critArr  = {"y": self.y, "e":self.epsilon}

    def getAccuracy(self):
        print("Statystyka dokladnosci:")
        print(df._method_[0]['string'], end=" : ")
        print(df._method_[0]['acc']({"x1": self.x1, "x2": self.x2}))

        print(df._method_[1]['string'], end=" : ")
        print(df._method_[1]['acc']({"y": self.y,}))

    def checkCriteria(self) -> bool:
        if self.chosenCriteria==0:
            self.initCrtArr()
            return df._method_[self.chosenMethod]["calc"](self.critArr)
        elif self.chosenCriteria==1:
            return self.iters==self.iterations

    def isRootAlready(self):
        if self.getVal(self.x1)==0:
            print("Lewa strona przedzialu jest miejscem zerowy")
            return self.rootNotify(self.x1)
        elif self.getVal(self.x2)==0:
            print("Prawa strona przedzialu jest miejscem zerowy")
            return self.rootNotify(self.x2)
        return False

    def getHalf(self) -> float:
        return (self.x1+self.x2)*0.5

    def bisect(self):
        self.y = self.getVal(self.getHalf())

    def rootNotify(self, x0, pre) -> float:
        print(f"Liczba iteracji: {self.iters}")
        print(f"{pre}: Ustalone przyblizenie miejsca zerowego w {x0}")
        return x0

    def checkDifferentSign(self) -> bool:
        return self.getVal(self.x1)*self.getVal(self.x2) < 0

    def start_bisection(self):
        self.x1 = self.a
        self.x2 = self.b
        self.iters = 0

        res = self.isRootAlready()
        if not type(res)==bool:
            return (self.rootNotify(res, "Bisekcja"), self.getVal(res))

        if not self.checkDifferentSign():
            print("Bisekcja: Warunek nie zostal spelniony")
            return False

        self.bisect()
        while not self.checkCriteria():
            if self.getVal(self.x1)*self.y < 0:
                self.x2 = self.getHalf()
            elif self.getVal(self.x2)*self.y < 0:
                self.x1 = self.getHalf()
            else:
                return (self.rootNotify(self.getHalf(), "Bisekcja"), self.y)
            self.bisect()
            self.iters += 1
        return (self.rootNotify(self.getHalf(), "Bisekcja"), self.y)

    #metoda stycznych
    def start_newton(self):
        self.x1 = self.a
        self.x2 = self.b
        self.iters = 0

        res = self.isRootAlready()
        if not type(res)==bool:
            return self.rootNotify(res, "Newton")

        if not self.checkDifferentSign():
            print("Newton: Warunek nie zostal spelniony")
            return False

        # Check which side (left/right) faster changes
        # Eliminate side where limit is const
        if abs(self.getVal_d(self.x1)) < abs(self.getVal_d(self.x2)):
            self.x1 = self.x2
            self.x2 = self.a
        elif abs(self.getVal_d(self.x1)) == abs(self.getVal_d(self.x2)):
            self.x1 = self.getHalf()

        self.y = self.getVal(self.x1)
        self.ydx = self.getVal_d(self.x1)

        while not self.checkCriteria():
            self.iters += 1
            if self.ydx==0:
                print("Newton: Pierwsza pochodna równa 0")
                print(f"Liczba iteracji: {self.iters}")
                return False
            self.x3 = self.x2
            self.x2 = self.x1
            self.x1 = self.x1-(self.y/self.ydx)
            self.y = self.getVal(self.x1)
            self.ydx = self.getVal_d(self.x1)

            x1x3close = (self.x1-self.x3)<self.cycle
            y1y3close = self.getVal(self.x1)-self.getVal(self.x3)<self.cycle
            x1x2far = (self.x1-self.x2)>(self.cycle*10)
            if x1x3close and y1y3close and x1x2far and self.iters>2:
                print(f"Otrzymalismy mozliwy cykl miedzy x1={self.x1} a x2={self.x2}")
                print(f"Liczba iteracji: {self.iters}")
                return (self.x1, self.getVal(self.x1))

        return (self.rootNotify(self.x1, "Newton"), self.getVal(self.x1))