import math

# Simple function with parameters
def greet(name):
    return f"Hello, {name}!"

# Function with multiple parameters
def add(a, b):
    return a + b

# Function with default parameters
def introduce(name, age=25):
    return f"{name} is {age} years old"

# Function with multiple return values
def get_coordinates():
    return 10, 20

# Function with *args (variable number of arguments)
def sum_numbers(*args):
    return sum(args)

def count(*args):
    return len(args)

# Function with **kwargs (keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function with docstring
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2

# Recursive function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Lambda function (anonymous)
square = lambda x: x ** 2

# Usage examples
if __name__ == "__main__":
    print(greet("Alice"))
    print(add(5, 3))
    print(introduce("Bob"))
    x, y = get_coordinates()
    print(sum_numbers(1, 2, 3, 4))
    print(calculate_area(5))
    print(factorial(5))
    print(square(4))
    print(count(1, 2, 3, 4))