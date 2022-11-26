#!/usr/bin/env python3

import re


def run(filename):
  with open(filename) as f:
    file_contents = f.readlines()
    call_numbers = file_contents[0].strip().split(',')
    
    bingo_cards = assemble_bingo_cards(file_contents)
    score = play_bingo(bingo_cards, call_numbers)
    print(score)


def assemble_bingo_cards(file_contents):
  bingo_cards = []
  bingo_card = []
  
  for line in file_contents[2:]:
    if line.strip() == '':
      bingo_card.append([0, 0, 0, 0, 0])
      bingo_cards.append(bingo_card)
      bingo_card = []
    else:
      bingo_card.append(re.split('\s+', line.strip()) + [0])
  
  bingo_card.append([0, 0, 0, 0, 0])
  bingo_cards.append(bingo_card)
  
  return bingo_cards


def play_bingo(bingo_cards, call_numbers):
  unmarked_sum = 0
  bingos = set()
  
  for call_number in call_numbers:
    j = 0
    print('Calling {}'.format(call_number))
    for bingo_card in bingo_cards:
      i = 0
      while i < 5:
        if call_number in bingo_card[i][0:5]:
          index = bingo_card[i].index(call_number)
          bingo_card[i][index] = (call_number, 1)
          bingo_card[i][5] += 1
          bingo_card[5][index] += 1
          i = 5
        i += 1
        
        if 5 in bingo_card[5] or 5 in [x[5] for x in bingo_card[0:5]]:
          print('BINGO on {}'.format(j))
          bingos.add(j)
          print(len(bingo_cards))
          print(len(list(bingos)))
          print(bingos)
          
          if len(list(bingos)) == len(bingo_cards):
            for x in bingo_card[0:5]:
              for y in x[0:5]:
                if isinstance(y, str):
                  unmarked_sum += int(y)
            print(unmarked_sum)
            print(call_number)
            return unmarked_sum * int(call_number)
      j += 1