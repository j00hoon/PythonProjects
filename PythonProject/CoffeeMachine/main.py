
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


order_menu = Menu()
coffee_part = CoffeeMaker()
money_part = MoneyMachine()

coffee_part.report()
money_part.report()

is_coffee_machine_off = False
while not is_coffee_machine_off:
    user_choice = str(input(f"What would you like? ({order_menu.get_items()}): "))
    if user_choice == "off":
        is_coffee_machine_off = True
    elif user_choice == "report":
        coffee_part.report()
        money_part.report()
    else:
        coffee_drink = order_menu.find_drink(user_choice)
        if coffee_part.is_resource_sufficient(coffee_drink) and money_part.make_payment(coffee_drink.cost):
            coffee_part.make_coffee(coffee_drink)
