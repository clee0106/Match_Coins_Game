"""
Program: Match Coins Gamme
Author: Colin Lee
Purpose: Run the Match Coins game.
Starter Code/Resources: Python Crash Course, 3rd Edition
Date: September 26, 2026
"""

from player import Player


def main():
    """Run the Match Coins game."""

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play = input("\nDo you want to toss the coins? (y/n): ")

    while play.lower() == "y":
        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("Its a Match! Player 1 wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("No Match! Player 2 wins a coin.")

        print(f"\nPlayer 1 has {player1.get_wallet()} coins.")
        print(f"Player 2 has {player2.get_wallet()} coins.")

        play = input("\nDo you want to toss again? (y/n): ")

      print("\n--- Final Score ---")
      print(f"Player 1: {player1.get_wallet()}")
      print(f"Player 2: {player2.get_wallet()}")
    
      if player1.get_wallet() > player2.get_wallet():
          print("Player 1 wins!")
      elif player2.get_wallet() > player1.get_wallet():
          print("Player 2 wins!")
      else:
          print("Its a draw!")


if __name__ == "__main__":
    main()
        
        
            
      
    
