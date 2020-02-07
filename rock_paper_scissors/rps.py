#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  choices = ('rock', 'paper', 'scissors')
  plays = []

  if n <= 0:
      return [plays]

  def options(n, plays = []):
    if n <= 0:
      return []

    for choice in choices:
      plays.append(choice)
      plays.append(options(n-1, plays))

    print(plays)

    return plays

  for choice in choices:
    plays.append([choice] + options(n, plays))


  return plays
  # pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')