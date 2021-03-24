import variables as df
import methods as meth
import plot as plt
from sys import float_info

class Interface():
    def __init__(self):
        self.createMethObj()
        self.start()

    def start(self):
        self.chooseFunction()
        self.setIntervals()
        self.chooseCriteria()
        self.setParameters()

    def calc(self):
        res_b, res_n = self.meth.calc_all()
        if type(res_b)==bool:
            res_b=False
        if type(res_n)==bool:
            res_n=False
        self.writeChart(res_b, res_n)
        print("")
        print(f"Przykładowe miejsca zerowe: {self.meth.exampleRoots()}")

    def writeChart(self, bisection, newton):
        nOfPoints = 100
        XY = self.meth.calcXY(nOfPoints)

        pointPlot = False
        if(newton and newton[0]<min(XY[0])):
            pointPlot=self.meth.calcXY(nOfPoints, newton[0], min(XY[0]))
        elif(newton and newton[0]>max(XY[0])):
            pointPlot=self.meth.calcXY(nOfPoints, max(XY[0]), newton[0])
        plt.plot(XY, bisection, newton, self.meth.getEquation(), pointPlot)

    def chooseFunction(self):
        print("Wybierz funkcję")
        index = self.showAndChoose(df._functions_)
        if not self.isDigit(index, len(df._functions_)):
            self.chooseFunction()
            return
        self.setMethVar("chosenFunction", int(index)-1)

    def chooseCriteria(self):
        print("Wybierz kryterium")
        index = self.showAndChoose(df._criteria_)
        if not self.isDigit(index, len(df._criteria_)):
            self.chooseCriteria()
            return
        self.setMethVar("chosenCriteria", int(index)-1)

    def setParameters(self):
        if self.meth.chosenCriteria == 0:
            self.chooseMethod()
            self.setEpsilon()
        elif self.meth.chosenCriteria == 1:
            self.setIterations()

    def chooseMethod(self):
        print("Wybierz metodę")
        index = self.showAndChoose(df._method_)
        if not self.isDigit(index, len(df._method_)):
            self.chooseMethod()
            return
        self.setMethVar("chosenMethod", int(index)-1)

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

    def setEpsilon(self):
        epsilon = input("Podaj epsilon: ")
        if not self.isFloat(epsilon):
            self.setEpsilon()
            return
        elif float(epsilon)<=0:
            print("Epsilon musi byc wiekszy od 0")
            self.setEpsilon()
            return
        epsilon=float(epsilon)
        self.setMethVar("epsilon", epsilon)
        print("")

    def setIterations(self):
        iterations = input("Podaj liczbę iteracji: ")
        if not self.isDigit(iterations, float_info.max):
            self.setIterations()
            return
        iterations = int(iterations)
        self.setMethVar("iterations", iterations)

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
    interface.calc()