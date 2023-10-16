import textwrap


class CoffeeMachine:
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

    def __init__(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.coffee_machine = {
            "water": water,
            "milk": milk,
            "beans": beans,
            "cups": cups,
            "money": money
        }

    def print_contents(self):
        print(textwrap.dedent(f"""\
        The coffee machine has:
        {self.coffee_machine['water']} ml of water
        {self.coffee_machine['milk']} ml of milk
        {self.coffee_machine['beans']} g of coffee beans
        {self.coffee_machine['cups']} disposable cups
        ${self.coffee_machine['money']} of money"""))

    def check_stock(self, coffee_type):
        for ingredient, amount in coffee_type.items():
            if abs(amount) > self.coffee_machine[ingredient]:
                return False, ingredient
        return True, None

    def make_coffee(self, coffee_type):
        for ingredient, amount in coffee_type.items():
            self.coffee_machine[ingredient] += amount
        self.coffee_machine["cups"] -= 1

    def buy_coffee(self):
        while True:
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n").lower()

            if choice == "back":
                return
            elif choice in self.coffee_types:
                break
            else:
                print("Invalid choice. Please select a valid option.\n")

        selected_coffee = self.coffee_types[choice]
        is_enough_stock, missing_ingredient = self.check_stock(selected_coffee)

        if not is_enough_stock:
            print(f"Sorry, not enough {missing_ingredient}!")
        else:
            print("I have enough resources, making you a coffee!")
            self.make_coffee(selected_coffee)

    def empty_cash_register(self):
        print(f"I gave you ${self.coffee_machine['money']}")
        self.coffee_machine['money'] = 0

    def fill_coffee_machine(self):
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
                        self.coffee_machine[ingredient] += amount
                        break
                except ValueError:
                    print("Invalid input. The value must be a non-negative integer.\n")

    def main(self):
        try:
            action = input("Write action (buy, fill, take, remaining, exit):\n").lower()
            print()

            while action != "exit":
                if action == "buy":
                    self.buy_coffee()
                elif action == "fill":
                    self.fill_coffee_machine()
                elif action == "take":
                    self.empty_cash_register()
                elif action == "remaining":
                    self.print_contents()
                action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
                print()
        except KeyboardInterrupt:
            print("The program has been interrupted.")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    coffee_machine.main()
