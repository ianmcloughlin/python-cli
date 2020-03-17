# Ian McLoughlin

import sys

try:
  with open(sys.argv[1]) as f:
    print(f.read())
except FileNotFoundError:
  print("File " + sys.argv[1] + " does not exist.")
