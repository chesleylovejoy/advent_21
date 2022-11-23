#!/usr/bin/env python3

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    x = 0
    y = 0
    
    for f in file_contents:
      direction = f.split(' ')[0]
      distance = f.split(' ')[1]
      
      if direction == 'forward':
        x += int(distance)
      elif direction == 'up':
        y -= int(distance)
      elif direction == 'down':
        y += int(distance)
      else:
        print('Unknown direction')

    print('Position: ({}, {})'.format(x, y))
    print(x * y)