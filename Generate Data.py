#!/usr/bin/env python3
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
        
        writer.writerow(["Number",
#                         "# of Divisors",
#                         "# of Factors",
#                         "Highly Composite",
#                         "Powerful",
#                         "Pronic",
#                         "Squarefree",
        
#                         "Fermat",
#                         "Fibonacci",
#                         "Lucas",
#                         "Mod 4",
                         "Mod 5",
                         "Mod 6",
                         "Prime"
#                         "Gaussian Prime"
                        ])

        for i in range(2, index):
#            countDivisors = tests.countDivisors(i)
#            countFactors = tests.countPrimeFactors(i, primes)
#            highlyComposite = tests.highlyComposite(i)
#            powerful = tests.powerful(i, primes)
#            pronic = tests.pronic(i)
#            squarefree = tests.squarefree(i, primes)

#            Fermat = tests.Fermat(i,2)
#            Fibonacci = tests.Fibonacci(i)
#            Lucas = tests.Lucas(i)
#            mod4 = tests.mod4(i)
            mod5 = tests.mod5(i)
            mod6 = tests.mod6(i)
            if i in primes:
                prime = 1
            else:
                prime = 0
#            Gauss = tests.GaussianPrime(i, primes)
            
            writer.writerow([str(i),
#                             str(countDivisors),
#                             str(countFactors),
#                             str(highlyComposite),
#                             str(powerful),
#                             str(pronic),
#                             str(squarefree),
            
#                             str(Fermat),
#                             str(Fibonacci),
#                             str(Lucas),
#                             str(mod4),
                             str(mod5),
                             str(mod6),
                             str(prime)
#                             str(Gauss)
                             ])

    return None

main(1474)