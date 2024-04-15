import numpy as np
from matplotlib import pyplot as plt
from fractions import Fraction


def find_root(f, df=None, start=0):
    # define the derivative of f if not specified
    if(df is None):
        def df(x, h=1e-12):
            return (f(x+h) - f(x)) / h

            
    # calculate the values using the function from the course
    calc_values = []
    x = start
    while x not in calc_values:
        calc_values.append(x)
        x = x - (f(x) / df(x))

        #exit clause for function where there is no root
        if(len(calc_values) >= 10**4):
            break
    return calc_values


def y(x):
    return x**3 + x - 16

values = find_root(y)
print(values[-1])

#2.387686553392325