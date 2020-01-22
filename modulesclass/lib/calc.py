if __name__ == "__main__":
    plus()
    minus()
    mult()
    dev()


def plus(*params):
    res = 0
    for item in params:
        res += item
    return res


def minus(a, b):
    return a - b


def mult(*params):
    res = 1
    for item in params:
        res *= item
    return res


def dev(a,b):
    if b == 0:
        return "Ділення на нуль!"
    else:
        return a/b
