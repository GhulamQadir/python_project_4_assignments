def getFirstElement(myList):
    firstElement:str = myList[0]
    return firstElement


def getList():
    myList:list[str]= []
    listElement:str=input("Enter list element or press enter:\t")
    while listElement!="":
        myList.append(listElement)
        listElement:str=input("Enter list element or press enter:\t")
    return myList


def main():
    myList:list[str] = getList()
    print(myList)
    firstElement:str = getFirstElement(myList)
    print(f"First element of the list is {firstElement}")
    
    
    
if __name__ == '__main__':
    main()