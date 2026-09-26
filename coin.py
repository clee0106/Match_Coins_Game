"""
Program: Match Coins Game
Author: Colin Lee
Purpose: Represent a coin that can be tossed.
Starter Code: None
Date: September 26, 2026
"""

import random


class Coin:
  """Represent a coin with a heads or tails side."""

  def __init__(self):
    """Initialize the coin with heads facing up."""
    self.__sideup = "Heads"

  def toss(self):
    """Randomly toss the coin."""
    if random.randint(0,1) == 0:
        self.__sideup = "Heads"
    else:
        self.__sideup = "Tails"

  def get_sideup(self):
      """Return the current side of the coin."""
      return self.__sideup
