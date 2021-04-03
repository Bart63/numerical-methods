import numpy as np
from horner import horner

#coeffs_d polynominal more accurate

# Array for all functions
_functions_ = []

# Linear
_linear_ = {
    "string" : "6x+0.9",
    "calc" : (lambda x : 6*x+0.9),
}
_functions_.append(_linear_)

# Absolute
_absolute_ = {
    "string" : "|x|",
    "calc" : (lambda x : np.absolute(x))
}
_functions_.append(_absolute_)

# Polynominal
_polynominal_ = {
    "coeffs" : [1,0,-5,0],
    "string" : "x(x-sqrt(5))(x+sqrt(5))",
    "calc" : (lambda x : horner(_polynominal_["coeffs"], x))
}
_functions_.append(_polynominal_)

_polynominal2_ = {
    "coeffs" : [1,0,-14,0,49,0,-36],
    "string" : "(x-3)(x-2)(x-1)(x+1)(x+2)(x+3)",
    "calc" : (lambda x : horner(_polynominal2_["coeffs"], x))
}
_functions_.append(_polynominal2_)

# Trigonometric
_trigonometric_ = {
    "string" : "sin(2⋅x) + cos(x)",
    "calc" : (lambda x : np.sin(x*2)+np.cos(x))
}
_functions_.append(_trigonometric_)

# Mixed
_mixed_ = {
    "string" : "|cos(6x+0.9)|-0.5",
    "calc" : (lambda x : abs(np.cos(6*x+0.9))-0.5)
}
_functions_.append(_mixed_)