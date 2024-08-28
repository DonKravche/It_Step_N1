# Python Advanced Concepts Practice

This repository contains a set of Python tasks designed to practice advanced concepts such as decorators, functors, and metaclasses.

## Tasks

### Task 1: Decorator for Positive Number Validation

Write a function that simply returns a number passed as an argument. Create a decorator that checks if the number is positive. If the number is negative, return a ValueError with an appropriate message. Otherwise, execute the function and print the result from the decorator.

### Task 2: Functor Implementation

Implement Task 1 using a functor instead of a decorator.

### Task 3: Execution Time Measurement Decorator

Create a decorator that calculates the execution time of a function and prints it to the terminal. Use `time.time()` to measure the time.

### Task 4: LoggingMeta Metaclass

Create a metaclass named `LoggingMeta` that prints the name of each class as it's being created.

## Getting Started

1. Clone this repository.
2. Each task should be implemented in a separate Python file.
3. Run each file to test your implementation.

## Requirements

- Python 3.x

## Tips

- For Task 1 and 3, remember that decorators are functions that take a function as an argument and return a new function.
- For Task 2, a functor in Python is typically implemented as a class with a `__call__` method.
- For Task 4, you'll need to override the `__new__` method of the metaclass.

## Example Usage

```python
# Task 1 example
@positive_number_decorator
def return_number(n):
    return n

print(return_number(5))   # Should print 5
print(return_number(-5))  # Should raise ValueError

# Task 3 example
@time_measurement_decorator
def some_function():
    # Some time-consuming operation
    pass

some_function()  # Should print execution time

# Task 4 example
class MyClass(metaclass=LoggingMeta):
    pass
# Should print "Creating class: MyClass"
```

Feel free to modify and expand upon these tasks as needed. Good luck and happy coding!