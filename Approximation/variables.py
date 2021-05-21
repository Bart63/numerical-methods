from math import pi
from numpy import cos, sqrt, sin
from horner import horner

# For Chebyshev polynominals:
w = lambda x: 1/sqrt(1-x*x)

# Array for all functions
_functions_ = []

# Linear
_linear_ = {
    "string" : "2x+3",
    "calc" : (lambda x : 2*x+3)
}
_functions_.append(_linear_)

# Absolute
_absolute_ = {
    "string" : "|x|",
    "calc" : (lambda x : abs(x))
}
_functions_.append(_absolute_)

# Polynominal
_polynominal_ = {
    "coeffs" : [1,0,-2, 0],
    "string" : "x(x-sqrt(2))(x+sqrt(2))",
    "calc" : (lambda x : horner(_polynominal_["coeffs"], x))
}
_functions_.append(_polynominal_)

# Trigonometric
_trigonometric_ = {
    "string" : "sin(2⋅x) + cos(x)",
    "calc" : (lambda x : sin(x*2)+cos(x))
}
_functions_.append(_trigonometric_)

# Mixed
_mixed_ = {
    "string" : "|cos(x·pi/2)|",
    "calc" : (lambda x : abs(cos(x*pi/2)))
}
_functions_.append(_mixed_)
