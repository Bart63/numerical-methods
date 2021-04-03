from functools import reduce
def horner(coeffs, X):
    return [reduce(lambda y,c: y*x+c, coeffs, 0)
            for x in X]