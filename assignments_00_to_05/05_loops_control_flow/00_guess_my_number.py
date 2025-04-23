import random


def main():
    secret_num: int = random.randint(0, 99)
    guessNum: str = int(input("Guess integer between (0,99):\t"))
    while guessNum != secret_num:
        if guessNum < secret_num:
            print("Your guess is lower than the secret number")
        else:
            print("Your guess is higher than the secret number")

        guessNum: str = int(input("Guess integer between (0,99):\t"))

    print(f"Congrats! The number was: {secret_num}")


if __name__ == "__main__":
    main()
