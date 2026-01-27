import art
print(art.logo)
print("Welcome to the Blackjack game!")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
import sys
computer_cards=[]
user_cards=[]
user_total=0
computer_total=0
play_or_not=input("Do you want to play Blackjack? (yes/no) ").lower()
if play_or_not=="yes":
    computer_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    user_total=sum(user_cards)
    computer_total=sum(computer_cards)
    print(f"Your cards are {user_cards} , total is {user_total} and computer's first card is {computer_cards[0]}")
    loop_over=False
    while not loop_over:
        user_total=sum(user_cards)
        computer_total=sum(computer_cards)
        if computer_total>21 or user_total>21:
            if user_total>21 and computer_total<21:
                print("You went over 21, you lose!")
                print(f"Your cards are {user_cards} , total is {user_total} and computer's cards are {computer_cards}")
                sys.exit()
            elif computer_total>21 and user_total<21:
                print("The computer went over 21, you win!")
                print(f"Your cards are {user_cards} , total is {user_total} and computer's cards are {computer_cards}")
                sys.exit()
        if user_total>21:
            if 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
                if user_total>21:
                    print("You went over 21, you lose!")
                    print(f"Your cards are {user_cards} , total is {user_total} and computer's cards are {computer_cards}")
                    sys.exit()
            if 11 not in user_cards:
                print("You went over 21, you lose!")
                print(f"Your cards are {user_cards} , total is {user_total} and computer's cards are {computer_cards}")
                sys.exit()
        another_card=input("Do you want to get another card? (yes/no) ").lower()
        if another_card=="yes":
            user_cards.append(random.choice(cards))
            continue
        loop_over=True
        if computer_total<17:
            while computer_total<17:
                computer_cards.append(random.choice(cards))
        if computer_total>21:
            print("The computer went over 21, you win!")
            print(f"Your cards are {user_cards} , total is {user_total} and computer's cards are {computer_cards}")
            sys.exit()
        if user_total>computer_total:
            print("You win, you have a higher total!")
            print(f"Your cards are {user_cards} , total is {user_total} and computer's cards are {computer_cards}")
            sys.exit()
        elif computer_total>user_total:
            print("The computer has a higher total, you lose!")
            print(f"Your cards are {user_cards} , total is {user_total} and computer's cards are {computer_cards}")
            sys.exit()
        elif computer_total==user_total:
            print("It's a draw, both you and computer have same scores!")
            print(f"Your cards are {user_cards} , total is {user_total} and computer's cards are {computer_cards}")
            sys.exit()
elif play_or_not=="no":
    print("Its alright")






