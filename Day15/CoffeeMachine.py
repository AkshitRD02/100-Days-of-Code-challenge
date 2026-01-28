MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}
def entercoins(cost):
    Nq=int(input("Enter the number of quarters: "))
    Nd=int(input("Enter the number of dimes: "))
    Nn=int(input("Enter the number of nickels: "))
    Np=int(input("Enter the number of pennies: "))
    total=((Nq*0.25)+(Nd*0.10)+(Nn*0.05)+(Np*0.01))
    if cost>total:
        print("Insufficient money given. Here is your amount.")
    elif cost<total:
        print(f"Transaction successful. Here is {(total-cost):.2f} change.")
    resources["money"]+=cost
def makecoffee(name,water,milk,coffee):
    resources["water"]-=water
    resources["milk"]-=milk
    resources["coffee"]-=coffee
    print(f"Here is your {name}. Enjoy your coffee!")





loop_over=False
while not loop_over:
    choice= input("What would you like? (expresso/latte/cappuccino):").lower()
    if choice == "off":
        loop_over = True
    elif choice == "report":
        print(resources)
    elif choice == "espresso":
        if resources["water"]>=MENU["espresso"]["ingredients"]["water"] and resources["coffee"]>=MENU["espresso"]["ingredients"]["coffee"]:
            print("Espresso costs 1.5 dollars. Please enter coins.")
            entercoins(1.5)
            makecoffee("Espresso",50,0,18)
        else:
            print("Not enough ingredients. Try again later.")
    elif choice == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >=MENU["latte"]["ingredients"]["coffee"] and resources["milk"] >=MENU["latte"]["ingredients"]["milk"]:
            print("Latte costs 2.5 dollars. Please enter coins.")
            entercoins(2.5)
            makecoffee("Latte",200,150,24)
        else:
            print("Not enough ingredients. Try again later.")
    elif choice == "cappuccino":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >=MENU["latte"]["ingredients"]["coffee"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            print("Cappuccino costs 3.0 dollars. Please enter coins.")
            entercoins(3.0)
            makecoffee("Cappuccino",250,100,24)
        else:
            print("Not enough ingredients. Try again later.")









