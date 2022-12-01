#!/usr/bin/env python3

def run(filename):
  with open(filename) as f:
    fish = [int(x) for x in f.read().strip().split(',')]
    
    for i in range(0, 80):
      new_fish = []
      for j,f in enumerate(fish):
        if f == 0:
          fish[j] = 6
          new_fish.append(8)
        else:
          fish[j] = f - 1
      fish += new_fish
    
    print(len(fish))
