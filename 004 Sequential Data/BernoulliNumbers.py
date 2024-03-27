from fractions import Fraction
import math
import time

factorial_dict = {0: Fraction(math.factorial(0)), 1: Fraction(math.factorial(1))}
def get_factorial(n):
    if n not in factorial_dict:
        factorial_dict[n] = math.factorial(n)
    return factorial_dict[n]




bernouli_dict = {0: Fraction(1)}
def get_bernouli_number(n):
    if n not in bernouli_dict:
        # here we calculate the bernouli value
        result = Fraction(0)
        for k in range(n):
            result -= Fraction(
                get_factorial(n) * get_bernouli_number(k),
                get_factorial(k) * get_factorial(n-k+1)
            )
        bernouli_dict[n] = result
    return bernouli_dict[n]



start = time.time()
print(get_bernouli_number(46))
print(time.time() - start)