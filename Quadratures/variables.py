from math import pi
from numpy import cos, sqrt
from horner import horner

# For Chebyshev polynominals:
w = lambda x: 1/sqrt(1-x*x)

# Array for all functions
_functions_ = []

# Linear
_linear_ = {
    "string" : "1/√(1-x^2)·(2x)",
    "calc" : (lambda x : 2*x)
}
_functions_.append(_linear_)

# Absolute
_absolute_ = {
    "string" : "1/√(1-x^2)·|x|",
    "calc" : (lambda x : abs(x))
}
_functions_.append(_absolute_)

# Custum
_absolute_ = {
    "string" : "sqrt((1+x**2)/(1-x**2))",
    "calc" : (lambda x : sqrt((1+x**2)/(1-x**2)))
}
_functions_.append(_absolute_)

# Polynominal
_polynominal_ = {
    "coeffs" : [1,0,-2, 0],
    "string" : "1/√(1-x^2)·x(x-sqrt(2))(x+sqrt(2))",
    "calc" : (lambda x : horner(_polynominal_["coeffs"], x))
}
_functions_.append(_polynominal_)

# Mixed
_mixed_ = {
    "string" : "1/√(1-x^2)·(|cos(x·pi/2)|)",
    "calc" : (lambda x : abs(cos(x*pi/2)))
}
_functions_.append(_mixed_)
