# checks if the current number is a prime number
def is_prime(number):
    if number <= 2: return true
    for n in range(2, number):
        if(number % n == 0):
            return False
    return True

# returns the next prime number after this one (not included)
def get_next_prime(number): 
    while True:
        number += 1
        if(is_prime(number)):
            return number

# splits the input number into its prime number
def split_primes(number):
    current = 2
    primes = []
    while number > 1:
        if(number % current == 0):
            primes.append(current)
            number /= current
            current = 2
        else:
            current = get_next_prime(current)
    return primes
