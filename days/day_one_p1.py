#!/usr/bin/env python3

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    less_than_even = []
    less_than_odd = []
    greater_than_even = []
    greater_than_odd = []
    
    for value in file_contents:
      value = int(value)
      if value <= 1000:
        if value % 2 == 0:
          less_than_even.append(value)
        else:
          less_than_odd.append(value)
      else:
        if value % 2 == 0:
          greater_than_even.append(value)
        else:
          greater_than_odd.append(value)
    
    found = compare_values(less_than_even, greater_than_even, 2020)
    if not found:
      compare_values(less_than_odd, greater_than_odd, 2020)
  
    
def compare_values(set_a, set_b, goal):
  for value_a in set_a:
    for value_b in set_b:
      if (value_a + value_b) == goal:
        print(value_a, value_b)
        print(value_a * value_b)
        return True
  return False
