#!/usr/bin/env python3
import random
import os
import sys
import time
from termcolor import colored 
 
def type(x): 
    for a in x:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.04) 
 
def clear(): # clears terminal
    os.system('cls' if os.name == 'nt' else 'clear') # nt - windows, else linux/mac
 
suits = ("Clubs", "Hearts", "Diamonds", "Spades")
ranks = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10")
restart = "\n\nWanna play again? Y/n "

dealer_lost = colored("Dealer lost! You Win!", "yellow", attrs=["blink"])

player_lost = colored("Dealer won! You lost!", "red", attrs=["blink"])


def main():
   os.system("clear")
   player_bank = 0
   dealer_bank = 0
   while True:
      ask = "\nHit or Stand?\n"
      print(ask)
      answer = input("")
      get_suit = random.choice(suits) 
   
      if answer.lower() == "h":
         type("\nPulling card for Player...\n\n")
         get_card_player = random.choice(ranks)
         player_bank += int(get_card_player)
         time.sleep(1.5)
         if get_card_player == "1":
            type(f"You got Ace of {get_suit}\n")
         if get_card_player == "10":
            nums = ("10", "Jack", "Queen", "King")
            tens = random.choice(nums)
            type(f"You got {tens} of {get_suit}\n")
         else: 
            type(f"You got {get_card_player} of {get_suit}\n")
         if player_bank > 21:
            type(f"You hit {player_bank}.\n{player_lost} ")
            time.sleep(1)
            type(restart)
            res = input("")
            if res.lower() == "y":
               os.system("clear")
               main()
            else:
               exit()
         if player_bank == 21:
            type("\nPlayer hit 21! ")
            type(f"\n{dealer_lost}")
            time.sleep(1)
            type(restart)
            res = input("")
            if res.lower() == "y":
               os.system("clear")
               main()
            else:
               exit()
         print(f"\nDealer cards: {dealer_bank} \nPlayer cards: {player_bank}") 
   
      elif answer.lower() == "s":
         type("\nPulling card for Dealer...\n\n")
         get_card_dealer = random.choice(ranks)
         def dealer():
            dealer = (f"Dealer gets {get_card_dealer} of {get_suit}\n")
            type(dealer)
         
         dealer_bank += int(get_card_dealer)
         time.sleep(1.5)
         if get_card_dealer == "1":
            type(f"Dealer got Ace of {get_suit}\n")
         if get_card_dealer == "10":
            num = ("10", "Jack", "Queen", "King")
            ten = random.choice(num)
            type(f"Dealer got {ten} of {get_suit}\n")
         else:
            dealer() 
         print(f"\nDealer cards: {dealer_bank} \nPlayer cards: {player_bank}")
         if dealer_bank >= 21:
            type(f"\nDealer hit {dealer_bank} ")
            type(f"\n{dealer_lost}")
            time.sleep(1)
            type(restart)
            res = input("")
            if res.lower() == "y":
               os.system("clear")
               main()
            else:
               exit()
         if dealer_bank == 21:
            type("\nDealer hit 21! ")
            type(colored("\n\nDealer won! You lost!", "red", attrs=["blink"]))
            time.sleep(1)
            type(restart)
            res = input("")
            if res.lower() == "y":
               os.system("clear")
               main()
            else:
               exit()
         if dealer_bank > float(player_bank) and dealer_bank < 22:
            type("\nDealer hit more than you! ")
            type(colored("\n\nDealer won! You lost!", "red", attrs=["blink"]))
            time.sleep(1)
            type(restart)
            res = input("")
            if res.lower() == "y":
               os.system("clear")
               main()
            else:
               exit()

main()
