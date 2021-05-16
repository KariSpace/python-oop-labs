class ExampleMeta(type):
 @classmethod
 def __prepare__(metacls, cls, bases):
    print(f'Metacls: {metacls} \n cls: {cls} \n bases: {bases}\n')
    print(f'Calling __prepare__ method of {super()}\n')
    return super().__prepare__(cls, bases)
 def __new__(metacls, cls, bases, dict):
    print(f'Calling __new__ method of {super()}\n')
    return super().__new__(metacls, cls, bases, dict)
 def __init__(self, cls, bases, dict):
    print(f'Calling __init__ method of {super()}\n')
    super().__init__(cls, bases,dict)
 
 def __call__(self, *args, **kwargs):
    print(f'Calling __call__ method of {super()}\n')
    return super().__call__(*args, **kwargs)


class A(metaclass=ExampleMeta):
  def __init__(self):
    print('This is when the new class instance gets created\n')
    print(f'Calling __init__ method of {self}')

a = A()