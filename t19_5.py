def checktype(cls):
    orig_init = cls.__init__

    def __init__(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)
        for fieldname, fieldvalue in self.__dict__.items():
            if not isinstance(fieldvalue, cls._field_type[fieldname]):
                raise TypeError(f"{fieldname} не є типом {cls._field_type[fieldname].__name__}")

    cls.__init__ = __init__
    return cls


@checktype
class TypeClass:

    _field_type = {"a": bool, "b": int, "c": float, "d": str}

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


if __name__ == '__main__':
    s1 = TypeClass(True, 1, 3.0, "4")
    s2 = TypeClass(False, 1, 2, "3")
