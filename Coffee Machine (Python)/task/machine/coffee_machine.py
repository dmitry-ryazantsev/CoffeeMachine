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


def check_stock(coffee_type):
    for ingredient, amount in coffee_type.items():
        if abs(amount) > coffee_machine[ingredient]:
            return False, ingredient
    return True, None


def make_coffee(coffee_type):
    for ingredient, amount in coffee_type.items():
        coffee_machine[ingredient] += amount
    coffee_machine["cups"] -= 1


def buy_coffee():
    while True:
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if choice == "back":
            return
        elif choice in coffee_types:
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

    selected_coffee = coffee_types[choice]
    is_enough_stock, missing_ingredient = check_stock(selected_coffee)

    if not is_enough_stock:
        print(f"Sorry, not enough {missing_ingredient}!")
    else:
        print("I have enough resources, making you a coffee!")
        make_coffee(selected_coffee)


def empty_cash_register():
    print(f"I gave you ${coffee_machine['money']}")
    coffee_machine['money'] = 0


def fill_coffee_machine():
    ingredient_prompts = {
        "water": "Write how many ml of water you want to add:",
        "milk": "Write how many ml of milk you want to add:",
        "beans": "Write how many grams of coffee beans you want to add:",
        "cups": "Write how many disposable cups of coffee you want to add:"
    }

    ingredients = ["water", "milk", "beans", "cups"]
    for ingredient in ingredients:
        while True:
            try:
                amount = int(input(ingredient_prompts[ingredient] + "\n"))
                if amount < 0:
                    raise ValueError
                else:
                    coffee_machine[ingredient] += amount
                    break
            except ValueError:
                print("Invalid input. The value must be a non-negative integer.\n")


if __name__ == "__main__":
    try:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        print("")

        while action != "exit":
            if action == "buy":
                buy_coffee()
            elif action == "fill":
                fill_coffee_machine()
            elif action == "take":
                empty_cash_register()
            elif action == "remaining":
                print_contents()
            action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
            print("")
    except KeyboardInterrupt:
        print("The program has been interrupted.")
