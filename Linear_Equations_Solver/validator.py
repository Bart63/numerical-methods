def isFloat(num) -> bool:
    try :
        float(num)
    except ValueError:
        print("Nie zmiennoprzecinkowa")
        return False
    return True

def isDigit(num, maximum) -> bool:
    if not num.isdigit():
        print("Zły typ")
        return False
    num = int(num)
    if not 1 <= num <= maximum:
        print("Nie w przedziale")
        return False
    return True