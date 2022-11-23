#!/usr/bin/env python3

import os
import argparse

basedir = "/Users/clovejoy/code/python/advent_21"

def make_files(day):
  os.system("cp {}/days/day_one_p1.py {}/days/day_{}_p1.py".format(basedir, basedir, day))
  os.system("cp {}/days/day_one_p2.py {}/days/day_{}_p2.py".format(basedir, basedir, day))
  os.system("touch {}/inputs/day_{}_p1_test.txt".format(basedir, day))
  os.system("touch {}/inputs/day_{}_p2_test.txt".format(basedir, day))
  os.system("touch {}/inputs/day_{}_p1.txt".format(basedir, day))
  os.system("touch {}/inputs/day_{}_p2.txt".format(basedir, day))


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='advent code')
  parser.add_argument('-d', '--day')

  args = parser.parse_args()

  make_files(args.day)
