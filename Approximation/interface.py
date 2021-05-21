import variables as df
import methods as meth
from sys import float_info

class Interface():
    def __init__(self):
        print("Autorzy: Bartosz Durys, Filip Hajek")
        print("Zadanie 5: Aproksymacja oparta o wielomiany Czebyszewa\n")
        self.noDegree = False
        self.createMethObj()
        self.start()

    def start(self):
        self.chooseFunction()
        self.setIntervals()
        self.setPolyDegree()
        if self.noDegree:
            self.setEpsilon()
        self.meth.startCalc()

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
        if a==b:
            self.setIntervals()
            return
        if a>b:
            a,b = b,a
        self.meth.setVars({"a": a, "b": b})
        
    def setPolyDegree(self):
        deg = input("Podaj stopień wielomianu (wprowadź 0 jak chcesz pominąć): ")
        if not self.isDigit(deg, min=0):
            self.setPolyDegree()
            return
        deg = int(deg)
        if deg==0:
            self.noDegree = True
            deg=1
        self.setMethVar("deg", deg)

    def setEpsilon(self):
        e = input("Podaj dokładność: ")
        if not self.isFloat(e):
            self.setEpsilon()
            return
        e = float(e)
        if e<=0.0:
            print("Epsilon musi być większy niż zero")
            self.setEpsilon()
            return
        self.setMethVar("eps", e)

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

    def isDigit(self, num, maximum=float_info.max, min=1) -> bool:
        if not num.isdigit():
            print("Zły typ")
            return False
        num = int(num)
        if not min <= num <= maximum:
            print("Nie w przedziale")
            return False
        return True

if __name__=="__main__":
    interface = Interface()