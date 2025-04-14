MAX_LENGTH: int = 3


def shortenList(shortList):
    while len(shortList) > MAX_LENGTH:
        removedElement: str = shortList.pop(-1)
        print(f"{removedElement} is remove from the list")
    return f"Now the updated list is: {shortList}"


def getList():
    myList: list[str] = []
    listElement: str = input("Enter list element or press enter:\t")
    while listElement != "":
        myList.append(listElement)
        listElement: str = input("Enter list element or press enter:\t")
    return myList


if __name__ == "__main__":
    myList: list[str] = getList()
    shortenedList = shortenList(myList)
    print(shortenedList)
