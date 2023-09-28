WATER_PER_CUP = 200
MILK_PER_CUP = 50
BEANS_PER_CUP = 15


def calculate_cups(water, milk, beans):
    possible_cups = min(water // WATER_PER_CUP, milk // MILK_PER_CUP, beans // BEANS_PER_CUP)
    return possible_cups


if __name__ == "__main__":
    water = int(input("Write how many ml of water the coffee machine has:\n"))
    milk = int(input("Write how many ml of milk the coffee machine has:\n"))
    beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
    cups = int(input("Write how many cups of coffee you will need:\n"))

    possible_cups = calculate_cups(water, milk, beans)

    if possible_cups == cups:
        print("Yes, I can make that amount of coffee")
    elif possible_cups > cups:
        extra_cups = possible_cups - cups
        print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
    elif possible_cups < cups:
        print(f"No, I can make only {possible_cups} cups of coffee")
