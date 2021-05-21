from functools import reduce
def horner_val(coeffs, x):
    return reduce(lambda y,c: y*x+c, coeffs, 0)

def horner(coeffs, X):
    if hasattr(X, "__getitem__"):
        return [horner_val(coeffs, x) for x in X]
    return horner_val(coeffs, X)