#!/usr/bin/env python3

from argparse import ArgumentParser
import importlib
import days

INPUT_FILE_PATH = '/Users/clovejoy/code/python/advent_21/inputs'


def run_test(day, part):
  script_name = 'day_{}_p{}'.format(day, part)
  file_name = '{}/day_{}_p{}_test.txt'.format(INPUT_FILE_PATH, day, part)
  script = importlib.import_module('days.{}'.format(script_name))
  script.run(file_name)


def run(day, part):
  script_name = 'day_{}_p{}'.format(day, part)
  file_name = '{}/day_{}_p{}.txt'.format(INPUT_FILE_PATH, day, part)
  script = importlib.import_module('days.{}'.format(script_name))
  script.run(file_name)


if __name__ == '__main__':
  parser = ArgumentParser(description='advent code')
  parser.add_argument('-t', '--test')
  parser.add_argument('-l', '--live')
  parser.add_argument('-d', '--day')
  parser.add_argument('-p', '--part')

  args = parser.parse_args()

  if args.test:
    run_test(args.day, args.part)
  else:
    run(args.day, args.part)
