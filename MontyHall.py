#!/usr/bin/env python3

#Monty Hall problem
import myLibrary as mh

#instantiate # of times to run simulation
n = 99999
#simulation simulates Monty Hall problem n times.
#simulation returns an array. 0th index = the 'gut' or 'no-switch' strategy success %,
#while the 1st index = the 'mathematical' or 'switch' strategy success %
simulation = mh.simulate(n)
print("Gut strategy percentage: ", simulation[0]) #
print("Math strategy percentage: ", simulation[1])

