def main():
    doubled_val: int = int(input("Enter any postive integer number"))
    print(doubled_val)
    while doubled_val < 100:
        doubled_val *= 2
        print(doubled_val)


if __name__ == "__main__":
    main()
