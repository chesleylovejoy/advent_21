#!/usr/bin/env python3

import math

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    found = False
    
    for i,value in enumerate(file_contents):
      if found:
        break
        
      less_than_even = []
      less_than_odd = []
      greater_than_even = []
      greater_than_odd = []
      value = int(value)
      other_values = file_contents[0:i] + file_contents[i+1:]

      goal = 2020 - value

      for other in other_values:
        other = int(other)
        if other <= math.ceil(goal/2):
          if other % 2 == 0:
            less_than_even.append(other)
          else:
            less_than_odd.append(other)
        else:
          if other % 2 == 0:
            greater_than_even.append(other)
          else:
            greater_than_odd.append(other)
    
      group_b = greater_than_even if goal % 2 == 0 else greater_than_odd
      group_c = greater_than_odd if goal % 2 == 0 else greater_than_even

      found = compare_values(less_than_even, group_b, value, goal)
      if not found:
        found = compare_values(less_than_odd, group_c, value, goal)


def compare_values(set_a, set_b, value, goal):
  for value_a in set_a:
    for value_b in set_b:
      if (value_a + value_b) == goal:
        print(value_a, value_b, value)
        print(value_a * value_b * value)
        return True
  return False