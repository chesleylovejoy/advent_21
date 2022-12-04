#!/usr/bin/env python3

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    count = 0
    
    for line in file_contents:
      split_line = line.split('|')
      inputs = split_line[0].strip().split(' ')
      outputs = split_line[1].strip().split(' ')
      
      for output in outputs:
        if len(output) in [2, 3, 4, 7]:
          count += 1
    
    print(count)
