def create_phone_book():
    phoneBook: dict = {}
    while True:
        name: str = input("Enter name:\t")
        if name != "":
            phoneNo: str = input("Enter phone number:\t")
            if phoneNo != "":
                phoneBook[name] = phoneNo
        if name == "" or phoneNo == "":
            break

    return phoneBook


def print_phone_book(phoneBook):
    for name, number in phoneBook.items():
        print(f"{name}: {number}")


def search_phone_num(phoneBook):
    lookUp: str = input("Do you want to look up for phone number?yes/no:\t").lower()
    if lookUp == "yes":
        nameToSearch: str = input(
            "Enter the name of the person you are searching for:\t"
        )
        if nameToSearch in phoneBook:
            print(f"{nameToSearch}: {phoneBook[nameToSearch]}")
        else:
            print(f"{nameToSearch} is not found in the phone book")


def main():
    phoneBook = create_phone_book()
    print_phone_book(phoneBook)
    search_phone_num(phoneBook)


# Python boilerplate.
if __name__ == "__main__":
    main()
