#!/usr/bin/env python3

import math

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    crabs = [int(x) for x in file_contents[0].strip().split(',')]
    crabs = sorted(crabs)
    
    crab_avg = sum(crabs) / len(crabs)
    print(crab_avg)
    
    # this is a little weird - the avg here is 486.505. I thought I should round that up,
    #   but it turns out it needs to be rounded down. I'm not entirely sure why - .5 rounding rules probably?
    #   Which means this code shouldn't be casting to 'int' - it should actually be using the rounding rules
    # crab_integer_avg = int(round(crab_avg, 0))
    crab_integer_avg = int(crab_avg)
    print(crab_integer_avg)
    
    fuel = 0
    for crab in crabs:
      fuel += sum([x for x in range(0, abs(crab - crab_integer_avg) + 1)])
    
    print(fuel)