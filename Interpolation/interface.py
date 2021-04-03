import variables as df
import methods as meth
from sys import float_info

class Interface():
    def __init__(self):
        print("Autorzy: Bartosz Durys, Filip Hajek")
        print("Zadanie 3: Metody interpolacji Lagrange'a i Newtona dla węzłów Czybyszewa\n")
        self.createMethObj()
        self.start()

    def start(self):
        self.chooseFunction()
        self.setIntervals()
        self.setCzebyshevPoints()
        self.meth.startCalc()

    def calc(self):
        print("")

    def writeChart(self):
        print("")

    def chooseFunction(self):
        print("Wybierz funkcję")
        index = self.showAndChoose(df._functions_)
        if not self.isDigit(index, len(df._functions_)):
            self.chooseFunction()
            return
        self.setMethVar("chosenFunction", int(index)-1)

    def createMethObj(self):
        self.meth = meth.Methods()

    def setIntervals(self):
        print("Stwórz przedział [a,b]")
        a = input("Podaj a: ")
        if not self.isFloat(a):
            self.setIntervals()
            return
        b = input("Podaj b: ")
        if not self.isFloat(b):
            self.setIntervals()
            return
        a = float(a)
        b = float(b)
        if a>b:
            self.meth.setVars({"a": b, "b": a})
        else:
            self.meth.setVars({"a": a, "b": b})

    def setCzebyshevPoints(self):
        points = input("Podaj liczbę węzłów Czybyszewa: ")
        if not self.isDigit(points, float_info.max):
            self.setCzebyshevPoints()
            return
        points = int(points)
        self.setMethVar("nofpoints", points)

    def showAndChoose(self, arr) -> str:
        for index, function in enumerate(arr):
            print(f"{index+1}. {function['string']}")
        return input("Index: ")

    def setMethVar(self, key, val):
        self.meth.setVars({key : val})

    def isFloat(self, num) -> bool:
        try :
            float(num)
        except ValueError:
            print("Nie zmiennoprzecinkowa")
            return False
        return True

    def isDigit(self, num, maximum) -> bool:
        if not num.isdigit():
            print("Zły typ")
            return False
        num = int(num)
        if not 1 <= num <= maximum:
            print("Nie w przedziale")
            return False
        return True

if __name__=="__main__":
    interface = Interface()