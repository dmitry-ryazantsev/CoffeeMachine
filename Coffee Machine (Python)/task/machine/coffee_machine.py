import textwrap

coffee_machine = {
    "water": 400,
    "milk": 540,
    "beans": 120,
    "cups": 9,
    "money": 550
}

espresso = {
    "water": -250,
    "beans": -16,
    "money": 4
}

latte = {
    "water": -350,
    "milk": -75,
    "beans": -20,
    "money": 7
}

cappuccino = {
    "water": -200,
    "milk": -100,
    "beans": -12,
    "money": 6
}

coffee_types = {
    "1": espresso,
    "2": latte,
    "3": cappuccino
}


def print_contents():
    print(textwrap.dedent(f"""\
    The coffee machine has:
    {coffee_machine['water']} ml of water
    {coffee_machine['milk']} ml of milk
    {coffee_machine['beans']} g of coffee beans
    {coffee_machine['cups']} disposable cups
    ${coffee_machine['money']} of money"""))


def buy_coffee():
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    for ingredient, amount in coffee_types[choice].items():
        coffee_machine[ingredient] += amount
    coffee_machine["cups"] -= 1


def empty_cash_register():
    print(f"I gave you ${coffee_machine['money']}")
    coffee_machine['money'] = 0


def fill_coffee_machine():
    water = int(input("Write how many ml of water you want to add:\n"))
    coffee_machine['water'] += water
    milk = int(input("Write how many ml of milk you want to add:\n"))
    coffee_machine['milk'] += milk
    beans = int(input("Write how many grams of coffee beans you want to add:\n"))
    coffee_machine['beans'] += beans
    cups = int(input("Write how many disposable cups of coffee you want to add:\n"))
    coffee_machine['cups'] += cups


if __name__ == "__main__":
    print_contents()
    action = input("\nWrite action (buy, fill, take):\n")

    if action == "take":
        empty_cash_register()
    elif action == "fill":
        fill_coffee_machine()
    elif action == "buy":
        buy_coffee()

    print("")
    print_contents()
