AFFIRMATION: str = "I am capable of doing anything I put my mind to."


def main():
    print(f"Please type the following affirmation: {AFFIRMATION}")
    user_input: str = input("")

    while user_input != AFFIRMATION:
        print(f"Please write the correct affirmation: {AFFIRMATION}")
        user_input: str = input("")

    print("Correct!")


if __name__ == "__main__":
    main()
