#!/usr/bin/env python3

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    i = 0
    increases = 0
    
    while i < len(file_contents) - 1:
      if int(file_contents[i]) < int(file_contents[i + 1]):
        increases += 1
      i += 1
    
    print(increases)
