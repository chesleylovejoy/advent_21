#!/usr/bin/env python3

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    i = 0
    increases = 0
    
    while i < len(file_contents) - 1:
      print(i)
      if (i + 2) < (len(file_contents)) and (i + 3) < (len(file_contents)):
        this_window = int(file_contents[i]) + int(file_contents[i + 1]) + int(file_contents[i + 2])
        next_window = int(file_contents[i + 1]) + int(file_contents[i + 2]) + int(file_contents[i + 3])
        if this_window < next_window:
          increases += 1
      i += 1
    
    print(increases)
