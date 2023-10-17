# Coffee Machine
This is a simple Python program for a coffee machine. The program allows users to interact with the coffee machine to buy coffee, refill its stock, take money from the cash register and check the current status of the machine.

## Features
1. Buy coffee: Choose from three different types of coffee (espresso, latte, cappuccino) and check whether the machine has enough ingredients to make your selection.
2. Fill coffee machine: Refill the coffee machine with water, milk, coffee beans and disposable cups.
3. Empty cash register: Retrieve the money earned from selling coffee.
4. Display remaining resources: Check the current status of the coffee machine, including the amount of water, milk, coffee beans, disposable cups and money in the cash register.
5. Exit the program: Quit the program and stop interacting with the coffee machine.

## Initial State
The program starts with the following initial resources:
- 400 ml of water
- 540 ml of milk
- 120 grams of coffee beans
- 9 disposable cups
- $550 in the cash register

## Usage
To run the Coffee Machine, execute the coffee_machine.py in a Python environment (the program was written in Python 3.8.3). When you start the program, you can enter commands as instructed.

## Example
```
Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
50 ml of water
465 ml of milk
100 g of coffee beans
8 disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
> fill

Write how many ml of water you want to add:
> 1000
Write how many ml of milk you want to add:
> 0
Write how many grams of coffee beans you want to add:
> 0
Write how many disposable cups you want to add:
> 0

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
1050 ml of water
465 ml of milk
100 g of coffee beans
8 disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 ml of water
390 ml of milk
80 g of coffee beans
7 disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit):
> take

I gave you $564

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 ml of water
390 ml of milk
80 g of coffee beans
7 disposable cups
$0 of money

Write action (buy, fill, take, remaining, exit):
> exit
```
