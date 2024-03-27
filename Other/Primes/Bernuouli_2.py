from fractions import Fraction
import math
import time

def factl(N):
    """
    Creates list of the first N factorial numbers.
    """
    l = []
    for n in range(N+1):
        a = 1
        for i in range(1,n+1):
            a = a*i
        l.append(a)
    return l

def bernoulli(n_target): # han n zu n_target umbenennt, wil ich d variable n unde wot bruche
    b = [Fraction(1)]
    l = factl(n_target+1)
    # sumk = b[0] -> sumk erscht im loop definiere, schüscht fasch nid für jedi bernouli zahl bi 0 a
    
    # du rechnisch ja alli bernoulli zahl i dem loop, han anstelle i, n brucht das es mit de formle stimmt
    for n in range(1, n_target+1):
        sumk = 0 # d summe machsch ja für jedi bernoulli zahl, darum definition im loop
        for k in range(n): # s summezeiche us de formle, jetzt eifach als for loop und nid als while
            termk = Fraction(
                l[n]*b[k],
                l[k]*l[n-k+1]
            ) # das isch s gliche wie du gha hesch, nur anstelle vo i wird jetzt n verwendet, denne stimmt mit de formle au
            sumk = sumk + termk # das isch s gliche wie du
        b.append(-sumk)
    return(b)

start = time.time()
print(bernoulli(1000))
print(time.time()-start, 's')