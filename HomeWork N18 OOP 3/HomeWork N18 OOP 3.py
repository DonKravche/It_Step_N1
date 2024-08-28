# 1
from datetime import time


def function_decorator(func):
    def wrapper(*args):
        if len(args) > 0 and isinstance(args[0], (int, float)) and args[0] > 0:
            return func(*args)
        else:
            return ValueError, f'Inputted value is less than 1.'

    return wrapper


@function_decorator
def function(number):
    return number


print(function(5))
print(function(-5))


# 2

class Functor:
    def __call__(self, *args):
        for numbers, arg in enumerate(args):
            if isinstance(arg, (int, float)) and arg < 0:
                return f"Argument at index {numbers} must be greater than or equal to zero"
        return args


f1 = Functor()
result = f1(1, 2, 3, 4, 5)
print(result)

f2 = Functor()
result = f2(1, 2, -3, 4, 5)
print(result)

# 3

import time


def function_decorator(func):
    def wrapper(*args):
        start_time = time.time()
        if len(args) > 0 and isinstance(args[0], (int, float)) and args[0] > 0:
            result = func(*args)
        else:
            result = ValueError, f'Inputted value is less than 1.'
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"ფუნქცია {func.__name__} შესრულდა {execution_time:.6f} წამში")
        return result

    return wrapper


@function_decorator
def function(number):
    return number


print(function(5))
print(function(-5))


# 4
class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating Class Name: {name}")
        return super().__new__(cls, name, bases, attrs)


class Logger(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name

    def return_name(self):
        return self.name


print(type(LoggingMeta))
print(type(Logger))


class AnotherClass(metaclass=LoggingMeta):
    pass
