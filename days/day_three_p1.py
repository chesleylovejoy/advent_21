#!/usr/bin/env python3

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    diagnostics = []
    gamma = ''
    epsilon = ''
    
    for line in file_contents:
      diagnostics.append(list(line.strip()))
    
    col_count = len(diagnostics[0])
    row_count = len(diagnostics)
    col = 0
    
    while col < col_count:
      col_sum = sum([int(x[col]) for x in diagnostics])
      if col_sum > (row_count / 2):
        gamma += '1'
        epsilon += '0'
      else:
        gamma += '0'
        epsilon += '1'
      col += 1
    
    print(gamma)
    print(epsilon)
    
    number = int(gamma, 2) * int(epsilon, 2)
    print(number)
