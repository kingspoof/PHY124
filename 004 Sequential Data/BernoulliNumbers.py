from fractions import Fraction
import math



bernouli_dict = {0: Fraction(1)}
def get_bernouli_number(n):
    if n not in bernouli_dict:
        # here we calculate the bernouli value
        result = Fraction(0)
        for k in range(n):
            result += Fraction(
                math.factorial(n) * get_bernouli_number(k),
                math.factorial(k) * math.factorial(n-k+1)
            )
        bernouli_dict[n] = (-1 * result)
    return bernouli_dict[n]

print(get_bernouli_number(46))