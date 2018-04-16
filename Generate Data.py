# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:16:21 2018

@author: NathanLHall
"""
import csv
import sequences
import tests

def main(index):
    primes = sequences.primes(index)
    with open("Data.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow(["Number","# of Divisors","# of Factors","Even","Fermat",
                         "Fibonacci","Gaussian Prime","Highly Composite","Mod 5",
                         "Mod 6","Powerful","Prime","Pronic","Squarefree"])

        for i in range(2, index):
            countDivisors = tests.countDivisors(i)
            countFactors = tests.countPrimeFactors(i, primes)
            even = tests.even(n)
            Fermat = tests.Fermat(i,2)
            Fibonacci = tests.Fibonacci(i)
            Gauss = tests.GaussianPrime(i, primes)
            highlyComposite = tests.highlyComposite(i)
            mod5 = tests.mod5(i)
            mod6 = tests.mod6(i)
            powerful = tests.powerful(i, primes)
            prime = i in primes
            pronic = tests.pronic(i)
            squarefree = tests.squarefree(i, primes)
            
            writer.writerow([str(i), str(countDivisors), str(countFactors),
                             str(even), str(Fermat), str(Fibonacci), str(Gauss),
                             str(highlyComposite), str(mod5), str(mod6),
                             str(powerful), str(prime), str(pronic), str(squarefree)])

    return None

main(37)
