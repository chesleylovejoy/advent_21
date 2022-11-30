#!/usr/bin/env python3

from collections import namedtuple

Line = namedtuple("Line", "x1 y1 x2 y2 points")

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    lines = []
    
    for line in file_contents:
      ordered_pairs = line.split('->')
      x1, y1 = ordered_pairs[0].strip().split(',')
      x2, y2 = ordered_pairs[1].strip().split(',')
      
      x1 = int(x1)
      y1 = int(y1)
      x2 = int(x2)
      y2 = int(y2)
      
      if x1 == x2 or y1 == y2:
        min_x = x1 if x1 < x2 else x2
        max_x = x2 if min_x == x1 else x1
        min_y = y1 if y1 < y2 else y2
        max_y = y2 if min_y == y1 else y1
        points = []
        
        for x in range(min_x, max_x + 1):
          for y in range(min_y, max_y + 1):
            points.append((x, y))
        lines.append(Line(x1, y1, x2, y2, points))
      else:
        print('Skipping {}'.format(line))
      
    
    intersections = {}
    for line in lines:
      for x, y in line.points:
        if (x, y) in intersections.keys():
          intersections[(x,y)] += 1
        else:
          intersections[(x,y)] = 1
    
    count = 0
    for key in intersections.keys():
      if intersections[key] > 1:
        count += 1
    
    print(count)