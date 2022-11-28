class ExceptNonEqual(Exception):

    def __init__(self):
        super()

    def __str__(self):
        return "not a string"


def decorator_line(f):
    def _decorator_line (*args, **kwargs):
        if f == str():
            raise ExceptNonEqual
        res = f(*args, **kwargs)
        return res
    return _decorator_line

@decorator_line
