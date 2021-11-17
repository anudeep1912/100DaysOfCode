from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    items = menu.get_items()
    coffee_type = input(f"What would you like ({items[0:-1]}): ").lower()
    if coffee_type == 'off':
        break
    item = menu.find_drink(coffee_type)
    if coffee_type == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        resources_available = coffee_maker.is_resource_sufficient(item)
        payment_successful = money_machine.make_payment(item.cost)
        if resources_available and payment_successful:
            coffee_maker.make_coffee(item)

