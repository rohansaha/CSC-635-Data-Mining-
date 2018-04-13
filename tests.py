# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:41:10 2018

@author: NathanLHall
"""

import math

'''True - 1
False - 0'''
def Euler(n, base):
    # n is the variable being tested for primality
    # base should be coprime to number
    if (base**((n - 1) / 2) - 1) % n == 0 or (base**((n - 1) / 2) + 1) % n == 0:
        return 1
    else:
        return 0
'''Even - 1
Odd - 0'''
def even(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

def factor(n, primes):
    factors = []
    if n <= 1:
        return factors
    while n > 1:
        for p in primes:
            if n % p == 0:
                factors.append(p)
                n = n // p
    return factors

'''True - 1
False - 0'''
def Fermat(n, base):
    # number is the variable being tested for primality
    # base should be coprime to number
    if n < 2:
        return None
    elif (base**(n - 1) - 1) % n == 0:
        return 1
    else:
        return 0


'''True - 1
False - 0'''
# Calculates the nth Fibonacci number
# This needs work
# It overflows if n gets too large
def Fibonacci(n):
    n += 1
    Phi = (math.sqrt(5) + 1) / 2
    phi = 1 - Phi
    
    fib = round(Phi**n - phi**n / math.sqrt(5))
    
    if fib % n == 0:
        return 1
    else:
        return 0

'''True - 1
False - 0'''
def GaussianPrime(n, primes):
    if n in primes and n % 4 == 3:
        return 1
    else:
        return 0

'''True - 1
False - 0'''
# Calculates the nth Lucas number
# if L_n 
def Lucas(n):
    n += 1
    if n == 0:
        lucas = 2
    elif n == 1:
        lucas = 1
    else:
        Phi = (math.sqrt(5) + 1) / 2
        phi = Phi - 1
        lucas = round(Phi**n + phi**n)
    
    if lucas % n == 0:
        return 1
    else:
        return 0

# Count the number of distinct divisors
def countDivisors(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count

# Count the number of distinct prime factors of a given number
def countPrimeFactors(n, primes):
    count = 0
    for p in primes:
        if n % p == 0:
            count += 1
    return count

'''True - 1
False - 0'''
# If a given number has more divisors than any natural number below it, it is highly composite
def highlyComposite(n):
    current = countDivisors(n)
    for i in range(1, n):
        count = countDivisors(i)
        if count >= current:
            return 0
    return 1

def mod4(i):
    result = i % 4
    return result

def mod5(i):
    result = i % 5
    return result

def mod6(i):
    result = i % 6
    return result

'''True - 1
False - 0'''
# If all the prime factors of a given number are repeated, it is a powerful number
def powerful(n, primes):
    factors = factor(n, primes)
    factors.sort()
    for i in range(len(factors)):
       count = factors.count(factors[i])
       if count == 1:
           return 0
    return 1

'''True - 1
False - 0'''
# If a given number is the product of k * (k + 1), it is pronic
def pronic(n):
    k = math.floor(math.sqrt(n))
    if n == k * (k + 1):
        return 1
    else:
        return 0

'''True - 1
False - 0'''
# If none of the prime factors of a given number are repeated, it is squarefree
def squarefree(n, primes):
    factors = factor(n, primes)
    factors.sort()
    for i in range(len(factors)):
        count = factors.count(factors[i])
        if count > 1:
            return 0
    return 1
