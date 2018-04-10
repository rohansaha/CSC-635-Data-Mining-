# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:04:28 2018

@author: NathanLHall
"""
import math

def Fibonacci(index):
    fibonacci = [1,1]
    for i in range(1,index - 2):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return fibonacci

def Lucas():
    lucas = [2,1]
    for i in range(1, index -2):
        lucas.append(lucas[-2] + lucas[-1])
    return lucas

def naturals(index):
    naturals = []
    for i in range(1, index):
        naturals.append(i)
    return naturals

def primes(index):
    primes = [2,3]
    candidate = 5
    while primes[-1] < index:
        modCandidate = checkDivisibility(candidate, primes)
        if type(modCandidate) == int:
            primes.append(candidate)
        candidate += 2
    return primes

def checkDivisibility(n, primes):
    for p in primes:
        if p > math.sqrt(n):
            break
        if n % p == 0:
            return None
    return n