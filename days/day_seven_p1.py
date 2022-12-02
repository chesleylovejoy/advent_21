#!/usr/bin/env python3

import math

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    crabs = [int(x) for x in file_contents[0].strip().split(',')]
    crabs = sorted(crabs)
    
    crab_median = ((crabs[int(len(crabs)/2)] + crabs[int(len(crabs)/2) - 1]) / 2) if len(crabs) % 2 == 0 else crabs[int(math.floor(len(crabs)/2)) + 1]
    
    print(crab_median)
    print(crabs)

    fuel = 0
    for crab in crabs:
      fuel += abs(crab - crab_median)
    
    print(fuel)