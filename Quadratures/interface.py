import variables as df
import methods as meth
from sys import float_info

class Interface():
    def __init__(self):
        print("Autorzy: Bartosz Durys, Filip Hajek")
        print("Zadanie 4: Całkowanie numeryczne złożoną kwadraturą Newtona-Cotesa oraz Gaussa w wariancie wielomianów Czebyszewa\n")
        self.createMethObj()
        self.start()

    def start(self):
        self.chooseFunction()
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

    def setEpsilon(self):
        e = input("Podaj dokładność:")
        if not self.isFloat(e):
            self.setIntervals()
            return
        e = float(e)
        if e<=0.0:
            print("Epsilon musi być większy niż zero")
            self.setIntervals()
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

    def isDigit(self, num, maximum, min=1) -> bool:
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