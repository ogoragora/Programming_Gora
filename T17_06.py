def decorator1_(f):
    def _decorator1_(*args, **kwargs):
        if kwargs:
            raise RuntimeError("Помилка, має ключові параметри")
        return f(*args, **kwargs)
    return _decorator1_


@decorator1_
def function(*args, **kwargs):
    if max(args) > sum(args):
        return 1
    s = 0
    for x in args:
        if x > 0:
            s += x
    return s

@decorator1_
def function1_(x):
    x += x
    return x

if __name__ == '__main__':
    print(function(3, 2, 4, -7, 8, 9)) #only args
    print(function(1, 3, x2=4)) #args and kwargs

