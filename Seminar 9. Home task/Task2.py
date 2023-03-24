class NewObjectMeta(type):
    a = None

    def __call__(a, *args, **kwargs):
        if a is None:
            a = super().__call__(*args, **kwargs)
        return a


class NewClass(metaclass=NewObjectMeta):
    pass


object_1 = NewClass()
object_2 = NewClass()
if object_1 is object_2:
    print("Объекты object_1 и object_2 явлются одним и тем же объектом.")
