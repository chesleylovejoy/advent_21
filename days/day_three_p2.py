#!/usr/bin/env python3

import copy

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
    
    ox_diag = copy.deepcopy(diagnostics)
    cs_diag = copy.deepcopy(diagnostics)
    
    while col < col_count:
      col_sum = sum([int(x[col]) for x in ox_diag])
      row_count = len(ox_diag)
      if col_sum >= (row_count / 2):
        ox_diag = [x for x in ox_diag if int(x[col]) == 1]
      else:
        ox_diag = [x for x in ox_diag if int(x[col]) == 0]
      print(len(ox_diag))
      if len(ox_diag) == 1:
        print(ox_diag)
        break
      col += 1

    col = 0
    while col < col_count:
      col_sum = sum([int(x[col]) for x in cs_diag])
      row_count = len(cs_diag)
      if col_sum >= (row_count / 2):
        cs_diag = [x for x in cs_diag if int(x[col]) == 0]
      else:
        cs_diag = [x for x in cs_diag if int(x[col]) == 1]
      if len(cs_diag) == 1:
        print(cs_diag)
        break
      col += 1
      
    print(len(cs_diag))
    
    number = int(''.join(ox_diag[0]), 2) * int(''.join(cs_diag[0]), 2)
    print(number)
