class prop:
    def __init__(self, fget=None, fset=None, fdel=None):
        print('init')
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        print('get')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("Getter method is not defined.")
        return self.fget(instance)

    def __set__(self, instance, value):
        print('set')
        if self.fset is None:
            raise AttributeError("Setter method is not defined.")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("Deleter method is not defined.")
        self.fdel(instance)

    def getter(self, fget):
        print('getter из prop')
        self.fget = fget
        return self

    def setter(self, fset):
        print('setter из prop')
        self.fset = fset
        return self

    def deleter(self, fdel):
        self.fdel = fdel
        return self


class Something:
    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        print('getter из Something')
        return self.x ** 2

    @attr.setter
    def attr_setter(self, update):
        print('setter из Something')
        self.x = update
        return self.x


s = Something(10)
print(s.attr)
# 100
s.attr = 3
print(s.attr)
9