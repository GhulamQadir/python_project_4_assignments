def get_nums():
    numList: list[int] = []
    while True:
        num: int = input("Enter integer to be added in list")
        if num == "":
            break
        else:
            numList.append(int(num))
    return numList


def check_nums(numList):
    numCheckDict: dict = {}
    for num in numList:
        if num not in numCheckDict:
            numCheckDict[num] = 1
        else:
            numCheckDict[num] += 1
    return numCheckDict


def num_count(checkNumDict: dict):
    for key, val in checkNumDict.items():
        print(f"{key} appears {val} time/s in a list")


if __name__ == "__main__":
    numList = get_nums()
    numCheckDict = check_nums(numList)
    num_count(numCheckDict)
