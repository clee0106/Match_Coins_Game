"""
Program: Match Coins Game
Author: Colin Lee
Purpose: Represent a player with a coin and a wallet.
Starter Code: Add accurate resource information.
Date: September 26, 2026
"""

from coin import Coin


class Player:
    """Represent a player in the Match Coins game."""

    def __init__(self,name):
        """Initialize the player's name, wallet, and coin."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Toss the player's coin."""
        self.__coin.toss()

    def get_coin_side(self):
        """Return the side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Remove one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the number of coins in the wallet."""
        return self.__wallet

    def get_name(self):
        """Return the player's name."""
        return self.__name
