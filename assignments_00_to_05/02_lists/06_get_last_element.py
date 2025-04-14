def getLastElement(myList):
    firstElement:str = myList[-1]
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
    lastElement:str = getLastElement(myList)
    print(f"Last element of the list is {lastElement}")
    
    
    
if __name__ == '__main__':
    main()