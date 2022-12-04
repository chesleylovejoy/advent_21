#!/usr/bin/env python3

OUTPUT_DICT = {
  'acedgfb': '8',
  'cdfbe': '5',
  'gcdfa': '2',
  'fbcad': '3',
  'dab': '7',
  'cefabd': '9',
  'cdfgeb': '6',
  'eafb': '4',
  'cagedb': '0',
  'ab': '1'
}

def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    
    count = 0
    digits = []
    sorted_output_dict = {}
    
    for k, v in OUTPUT_DICT.items():
      sorted_key = sorted(list(k))
      sorted_output_dict[''.join(sorted_key)] = v
    
    for line in file_contents:
      split_line = line.split('|')
      inputs = split_line[0].strip().split(' ')
      outputs = split_line[1].strip().split(' ')
      
      for output in outputs:
        print(output)
        digit = get_digit(output, sorted_output_dict)
        print(digit)
        digits.append(digit)
      print(''.join(digits))
      count += int(''.join(digits))
      digits = []
    
    print(count)

def get_digit(output, sorted_output_dict):
  if len(output) == 2:
    return '1'
  elif len(output) == 3:
    return '7'
  elif len(output) == 4:
    return '4'
  elif len(output) == 7:
    return '8'
  else:
    output_as_list = list(output)
    output_as_list = sorted(output_as_list)
    print(''.join(output_as_list))
    return sorted_output_dict[''.join(output_as_list)]


