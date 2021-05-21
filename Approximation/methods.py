from horner import horner
from math import pi, cos, sqrt

from numpy.lib.function_base import append
import variables as df
from plot import plot, plot_error
import numpy as np

class Methods():
    #wraz ze stopniem wielomianu - wykres bledow
    #wraz ze wzrostem wielomianu - blad 
    def __init__(self) -> None:
        self.x = []
        self.y = []
        self.poly = []
        self.app_x = []
        self.app_y = []
        self.errors = []

    def reset_vars(self):
        self.x = []
        self.y = []
        self.poly = []
        self.app_x = []
        self.app_y = []

    def getEquation(self) -> str:
        return df._functions_[self.chosenFunction]["string"]

    def setVars(self, kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def getVal(self, x) -> float:
        return df._functions_[self.chosenFunction]["calc"](x)

    def startCalc(self):
        self.get_nodes()
        self.get_chebyshev_poly()
        self.coeff_chebyshef()
        self.approximation()
        self.get_error()
        print("Maximum error: ", self.error, " Degree: ", self.deg)
        self.errors.append(self.error)
        if hasattr(self, 'eps') and self.error>self.eps:
            self.deg+=1
            self.reset_vars()
            self.startCalc()
            return
        X = np.arange(self.a, self.b, 0.01)
        Y = self.getVal(X)
        plot((X,Y), (self.app_x, self.app_y), self.getEquation())
        if len(self.errors)>1:
            plot_error(self.errors, self.getEquation())

    def get_chebyshev_poly(self):
        poly=self.poly
        for i in range(len(self.poly), self.deg+1):
            if i==0:
                poly.append([1])
            elif i==1:
                poly.append([1,0])
            else:
                for j in range(i, self.deg+1):
                    temp=[]
                    for k in range(0, j+1):
                        if k==0: temp.append(2*poly[j-1][0])
                        elif k==1: temp.append(0)
                        elif k==j: 
                            if j%2==1: temp.append(0)
                            else: temp.append(-poly[j-2][k-2])
                        else: temp.append(2*poly[j-1][k]-poly[j-2][k-2])
                    poly.append(temp)
        self.poly=poly

    def get_nodes(self):
        m = self.deg+1
        for i in range(1, m+1):
            curr_node = cos(((2*i-1)*pi)/(2*m))
            scaled_node = (curr_node+1)*((self.b-self.a)/2)+self.a
            self.x.append(curr_node)
            self.y.append(self.getVal(scaled_node))

    def gauss_chebyshev(self, num):
        weight=pi/self.deg
        m = self.deg+1
        numr, denum = 0, 0
        for i in range(0, m):
            poly_val = horner(self.poly[num], self.x[i])
            numr += weight*self.y[i]*poly_val
            denum += weight*poly_val*poly_val
        return numr/denum

    def coeff_chebyshef(self):
        self.coeff_ch = [self.gauss_chebyshev(i) for i in range(self.deg+1)]

    def approximation(self):
        a,b = self.a,self.b
        i=a
        while i<=b:
            next_app = [self.coeff_ch[j]*horner(self.poly[j], 2*(i-a)/(b-a)-1) for j in range(self.deg+1)]
            next_app=sum(next_app)
            self.app_x.append(i)
            self.app_y.append(next_app)
            i+=0.01
    
    def get_error(self):
        self.error = max([abs(app_y-self.getVal(self.app_x[i])) for i,app_y in enumerate(self.app_y)])
