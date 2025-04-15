def main():
    year: int = int(input("Enter any year:\t"))
    if year >= 1582:
        if year % 4 == 0:
            if year % 100 != 0:
                print(f"{year} is a leap year")
            elif year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print("Year should be greater than 1582")


if __name__ == "__main__":
    main()
