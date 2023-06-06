from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_list = Menu()


# TODO: 1. check user input
machine_on = True
while machine_on:
    options = menu_list.get_items()
    user_coffee_type = input(f"What would you like? {options}: ").lower()
    if user_coffee_type == "off":
        machine_on = False
    elif user_coffee_type == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu_list.find_drink(user_coffee_type)
        print(drink.ingredients)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
