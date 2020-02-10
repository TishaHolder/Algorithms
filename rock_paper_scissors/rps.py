#!/usr/bin/python
"""
Permutation is an arrangement of objects in a specific order. Order of arrangement of object is very important. 
The number of permutations on a set of n elements is given by  n!.  For example, there are 2! = 2*1 = 2 
permutations of {1, 2}, namely {1, 2} and {2, 1}, and 3! = 3*2*1 = 6 permutations of {1, 2, 3}, namely 
{1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2} and {3, 2, 1}.
"""

import sys
from itertools import permutations 


def rock_paper_scissors(n):

  game = []
  
  if n == 0:
    return [[]]
  if n == 1:
    return [['rock'], ['paper'], ['scissors']]
  if n == 2:
    return [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
  else:
    for possibilities in rock_paper_scissors(n - 1):        
        game.append(possibilities + ["rock"])
        game.append(possibilities + ["paper"])
        game.append(possibilities + ["scissors"])

  return game

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')