#!/usr/bin/env python3

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    x = 0
    y = 0
    aim = 0
    
    for f in file_contents:
      direction = f.split(' ')[0]
      distance = f.split(' ')[1]
      
      if direction == 'forward':
        x += int(distance)
        y += (aim * int(distance))
      elif direction == 'up':
        aim -= int(distance)
      elif direction == 'down':
        aim += int(distance)
      else:
        print('Unknown direction')
    
    print('Position: ({}, {})'.format(x, y))
    print(x * y)