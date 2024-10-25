# %%
class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10
    def get_private_field(self):
        return self.__private_field


foo = MyObject()
#foo.__private_field = 1000
#foo.get_private_field()
#assert foo.public_field == 5
#assert foo.__private_field == 10

# %%
class MyOtherObject:
    def __init__(self):
        self.__private_field = 71

    #@classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

bar = MyOtherObject()
assert MyOtherObject().get_private_field_of_instance(bar) == 71

# %%
class MyParentObject:
    def __init__(self):
        self.__private_field = 71

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

baz = MyChildObject()
#assert baz.get_private_field() == 71
assert baz._MyParentObject__private_field == 71
print(baz.__dict__)


# %%
class MyStringClass:
    def __init__(self, value):
        self.__value = value
        self.value = value
    def get_value(self):
        return str(self.__value)

foo = MyStringClass(5)
assert foo.get_value() == '5'
assert foo.value == 5

class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)

foo = MyIntegerSubclass('5')
assert foo.get_value() == 5

# %%
class MyBaseClass:
    def __init__(self, value):
        self.__value = value
    def get_value(self):
        return self.__value

class MyStringClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value())

class MyIntegerSubclass(MyStringClass):
    def get_value(self):        # Updated
        print(self.__dict__)
        return int(self._MyStringClass__value)  # Not updated

foo = MyIntegerSubclass(5)
foo.get_value()  

# %%
class MyStringClass:
    def __init__(self, value):
        # This stores the user-supplied value for the object.
        # It should be coercible to a string. Once assigned in
        # the object it should be treated as immutable.
        self._value = value

# %%
class ApiClass:
    def __init__(self):
        self._value = 5
    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # Conflicts

a = Child()
print(f'{a.get()} and {a._value} should be different')

# %%
class ApiClass:
    def __init__(self):
        self.__value = 5
    def get(self):
        return self.__value # Double underscore

class Child(ApiClass):
    def __init__(self): # Double underscore
        super().__init__()
        self._value = 'hello'  # OK!

a = Child()
print(f'{a.get()} and {a._value} are different')

# %%
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# %%
