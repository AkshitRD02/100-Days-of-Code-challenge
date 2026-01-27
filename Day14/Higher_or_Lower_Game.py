import art
from game_data import data
import random
print(art.logo)
random.shuffle(data)
x=49
i=0
while x>0:
    print("Who has more followers?")
    print(f"{data[i]["name"]}, a {data[i]["description"]} from {data[i]["country"]}")
    print(art.vs)
    print(f"{data[i+1]["name"]}, a {data[i+1]["description"]} from {data[i+1]["country"]}")
    choice=input("Enter first or second : ").lower()
    if choice == "first":
        if data[i]["follower_count"]>data[i+1]["follower_count"]:
            print(f"You are correct! Current score: {i+1}")
            print("\n"*20)
            x-=1
            i+=1
        elif data[i+1]["follower_count"]>data[i]["follower_count"]:
            print("You are wrong!")
            print("Game Over")
            x=0
    elif choice == "second":
        if data[i+1]["follower_count"]>data[i]["follower_count"]:
            print(f"You are correct! Current score: {i+1}")
            print("\n"*20)
            x-=1
            i+=1
        elif data[i]["follower_count"]>data[i+1]["follower_count"]:
            print("You are wrong!")
            print("Game Over")
            x=0
if i==48:
    print("You beat the whole game! WOW!")

