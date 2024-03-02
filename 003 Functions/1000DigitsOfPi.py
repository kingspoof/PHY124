import numpy as np
import sys
from fractions import Fraction
from decimal import Decimal
import time

# start a timer, so we can calculate the time it takes to run this
start = time.time()

# calculating T value using recursion,
# please ignore this, using this function will increase runtime to 15 seconds
def get_t_value_at_recursion(value, index) -> Fraction:
    if(index == 0): 
        return value
    else:
        return Fraction(-1 * value**2 * get_t_value_at_recursion(value, index -1))


t_value_dict = {}
def get_t_value(value, index):
    if(index == 0): 
        t_value_dict['0'] = Fraction(value)
    elif str(index) not in t_value_dict:
        t_value_dict[str(index)] = Fraction(-1 * value**2 * get_t_value(value, index-1))
    return t_value_dict[str(index)]


# calculates the taylor expansion, a depth of 200 yeals the precision required for 1'000 digits
def arctan_taylor_expansion(value, depth=2000):
    res = Fraction(0)
    for i in range(depth + 1):
        res += Fraction(get_t_value(value, i), Fraction(2*i + 1))
    return res

# formats the result according to the video explanation in the course
def format_result(result):
    result_int = int(result)
    result_float = result - result_int
    result_1000 = int(10**1000 * result_float)
    output_string = ('.'.join([str(result_int), str(result_1000)]))
    return output_string


value_3 = arctan_taylor_expansion(Fraction(1,3))
t_value_dict = {}
value_2 = arctan_taylor_expansion(Fraction(1,2))

result = Fraction(4,1) * (value_2 + value_3)
output_string = format_result(result)
print(output_string)
print(time.time() - start)

#print(get_t_value_at_recursion(Fraction(1,2), 50))
#print(get_t_value(Fraction(1,2), 50))