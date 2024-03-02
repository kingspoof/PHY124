import math

def neg_one_to_power(power: float) -> float:
    return (-1)**power

def get_numbered_odd(index: int) -> int:
    return 2*index + 1

def raise_to(base: float, exponent: float) -> float:
    return base**exponent

def factorial(number: int) -> int:
    result = 1
    for i in range(number, 0, -1):
        result *= i 
    return result

def sin_expansion(number):
    result = 0
    for i in range(50):
        top = neg_one_to_power(i) * raise_to(number, get_numbered_odd(i))
        bottom = factorial(get_numbered_odd(i))
        result += top/bottom
    return result