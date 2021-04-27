from math import pi, cos
import variables as df
from plot import plot
import numpy as np

class Methods():
    def getEquation(self) -> str:
        return df._functions_[self.chosenFunction]["string"]

    def setVars(self, kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def getVal(self, x) -> float:
        return df._functions_[self.chosenFunction]["calc"](x)

    def startCalc(self):
        print("Newton-Cotes:", self.newton_cotes())
        min_nodes, max_nodes = 2,5
        print("Czebyszew-Gauss:")
        for i in range(min_nodes, max_nodes+1):
            print("Dla", i, "węzłów:", self.gauss_chebyshev(i))
        X = np.linspace(-1, 1, 100)
        Y = self.getVal(X)
        plot((X,Y), self.getEquation())

    def simpson(self, a, b):
        h = (b-a)*0.5
        half = (a+b)*0.5
        f_1 = self.getVal(a)
        f_2 = self.getVal(half)
        f_3 = self.getVal(b)
        return (df.w(a)*f_1 + 4*df.w(half)*f_2 + df.w(b)*f_3)*h/3

    def complex_simpson(self, a_, b_):
        integral = self.simpson(a_, b_)
        enough, n = False, 1
        while not enough:
            new_integral = 0
            h = (b_-a_)/(2*n)
            a, b = a_, a_+h
            for _ in range(2*n):
                new_integral += self.simpson(a, b)
                a = b
                b += h
            n += 1
            enough = abs(new_integral - integral) < self.eps
            integral = new_integral
        return integral

    def newton_side(self, delta):
        a, sums = 0, 0
        i = 1
        enough = False
        while not enough:
            i *= 2
            l = [a, a + delta]
            l.sort()
            integral = self.complex_simpson(*l)
            sums += integral
            a += delta
            delta *= abs(delta)
            enough = abs(integral) <= abs(self.eps)
        return sums

    def newton_cotes(self):
        delta = 0.5
        return self.newton_side(delta)+self.newton_side(-delta)

    def gauss_chebyshev(self, nodes):
        weight = pi/nodes
        curr_node, res = 0, 0
        for i in range(1, nodes):
            curr_node = cos(((2*i-1)*pi)/(2*nodes))
            res += weight * self.getVal(curr_node)
        return res