#!/usr/bin/env python3

import copy

def run(filename):
  with open(filename) as f:
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    fish = [int(x) for x in f.read().strip().split(',')]
    
    for f in fish:
      counts[f] += 1
    
    for i in range(0, 256):
      new_counts = copy.deepcopy(counts)
      j = len(counts) - 1
      while j >= 0:
        if j == 0:
          # take everything in 0 and duplicate it to 8, move it to 6
          new_counts[8] = counts[j]
          new_counts[6] += counts[j]
        else:
          # take everything in j and move it to j-1
          new_counts[j - 1] = counts[j]
        j -= 1
      counts = new_counts
      
    print(sum(counts))