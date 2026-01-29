from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
espresso = MenuItem("espresso",50,0,18,1.5)
latte = MenuItem("latte",200,150,24,2.5)
cappuccino = MenuItem("cappuccino",250,100,24,3.0)
menu = Menu()
money_machine = MoneyMachine()
loop_over=False
while not loop_over:
    choice=input("What would you like? (espresso/latte/cappuccino/): ")
    if choice=="off":
        loop_over=True
    if choice=="report":
        coffee_maker.report()
    elif choice=="espresso":
        if coffee_maker.is_resource_sufficient(espresso):
            if money_machine.make_payment(1.5):
                coffee_maker.make_coffee(espresso)
    elif choice=="latte":
        if coffee_maker.is_resource_sufficient(latte):
            if money_machine.make_payment(2.5):
                coffee_maker.make_coffee(latte)
    elif choice=="cappuccino":
        if coffee_maker.is_resource_sufficient(cappuccino):
            if money_machine.make_payment(3.0):
                coffee_maker.make_coffee(cappuccino)



