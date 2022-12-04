#!/usr/bin/env python3

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    low_points = []
    risk = 0
    
    for i,line in enumerate(file_contents):
      line  = list(line.strip())
      for j,x in enumerate(line):
        x = int(x)
        up = 9 if i == 0 else int(file_contents[i - 1][j])
        down = 9 if i == len(file_contents) - 1 else int(file_contents[i + 1][j])
        left = 9 if j == 0 else int(line[j - 1])
        right = 9 if j == len(line) - 1 else int(line[j + 1])
        if min([x, up, down, left, right]) == x and x not in [up, down, left, right]:
          low_points.append((x, i, j))
          risk += x + 1
    #1568 is too high
    
    print(low_points)
    print(risk)
        
        
