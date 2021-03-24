import numpy as np
from horner import horner
from math import pi, e, sqrt

#coeffs_d polynominal more accurate

# Array for all functions
_functions_ = []

# Polynomial
_polynominal_ = {
    "coeffs" : [1,(10*pi+21.37-e),(213.7*pi-21.37*e-10*pi*e),(-213.7*pi*e)],
    "coeffs_d" : [3, (20*pi-2*e+2*21.37), (213.7*pi-21.37*e-10*pi*e)],
    "string" : "(x-e)(x+10pi)(x+21.37)",
    "calc" : (lambda x : horner(_polynominal_["coeffs"], x)),
    "calc_d" : (lambda x : horner(_polynominal_["coeffs_d"], x)),
    "roots" : f"{e:.20f}, {(-10*pi):.20f}, -21.37"
}
_functions_.append(_polynominal_)

_polynominal2_ = {
    "coeffs" : [1,0,-5,0],
    "coeffs_d" : [3, 0, -5],
    "string" : "x(x-sqrt(5))(x+sqrt(5))",
    "calc" : (lambda x : horner(_polynominal2_["coeffs"], x)),
    "calc_d" : (lambda x : horner(_polynominal2_["coeffs_d"], x)),
    "roots" : f"0, {-(sqrt(5)):.20f}, {(sqrt(5)):.20f}"
}
_functions_.append(_polynominal2_)

# Trigonometric
_trigonometric_ = {
    "string" : "sin(2*x) + cos(x)",
    "calc" : (lambda x : np.sin(2*x)+np.cos(x)),
    "calc_d" : (lambda x : 2*np.cos(2*x)-np.sin(x)),
    "roots" : "1.57079632679489661923 \n pi*n-(pi/2)"
    + "\n 2pi*n-(5pi/6) \n 2pi*n-(pi/6)"
}
_functions_.append(_trigonometric_)

# Exponential
_exponential_ = {
    "string" : "pi - 10^x ",
    "calc" : (lambda x : pi-10**x),
    "calc_d" : (lambda x : -10**x*np.log(10)),
    "roots" : "0.49714987269413385435"
}
_functions_.append(_exponential_)

# Mixed
_mixed_ = {
    "string" : "cos(exp(x))",
    "calc" : (lambda x : np.cos(np.exp(x))),
    "calc_d" : (lambda x : -np.exp(x)*np.sin(np.exp(x))),
    "roots" : "0.45158270528945486472 \n log(pi*n - pi/2)"
}
_functions_.append(_mixed_)

# Accuracy method
_method_ = [
    {
         "string" : "|xi - xi-1| < ε",
         "calc" : (lambda kwargs : abs(kwargs["x2"]-kwargs["x1"])<kwargs["e"]),
         "acc" : (lambda kwargs : abs(kwargs["x2"]-kwargs["x1"]))
    },

    {
         "string" : "|f(xi)| < ε",
         "calc" : (lambda kwargs : abs(kwargs["y"])<kwargs["e"]),
         "acc" : (lambda kwargs : abs(kwargs["y"]))
    }
]

# End algorithm criteria
_criteria_ = [
    {
         "string" : "Dokładność"
    },
    {
         "string" : "Liczba iteracji"
    }
]