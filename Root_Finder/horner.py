from functools import reduce
def horner(coeffs, x) -> float:
    return reduce(lambda y,c: y*x+c, coeffs, 0)