MAX_VALUE: int = 10_000


def main():
    first_term: int = 0
    second_term: int = 1
    next_term = 0
    print(first_term)
    print(second_term)
    while (next_term + second_term) < MAX_VALUE:
        next_term = second_term + first_term
        first_term = second_term
        second_term = next_term
        print(next_term)


if __name__ == "__main__":
    main()
