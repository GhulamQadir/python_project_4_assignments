def main()->list[str]:
    myList:list[str] = []
    listVal:str = input("Enter list element:\t")
    while listVal !="":
        myList.append(listVal)
        listVal:str = input("Enter list element:\t")
    return myList    


if __name__ == '__main__':
    getList=main()
    print(f"Here is your list: {getList}")