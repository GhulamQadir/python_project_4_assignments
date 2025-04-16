fruits: dict = {"apple": 10.7, "mango": 15.5, "banana": 4.3, "orange": 13.8}


def main():
    total = 0
    for fruit, price in fruits.items():
        quantity: int = int(input(f"How many {fruit}s do you want to buy:\t"))
        total += price * quantity
    return total


if __name__ == "__main__":
    total = main()
    print(f"Your total amount is {total} rupees")
