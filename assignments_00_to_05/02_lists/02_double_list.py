def main():
    numList:list[int] =[3,5,2,8]
    for index,value in enumerate(numList):
        squareOfNum:int = value**2
        numList[index] = squareOfNum 
    return numList



if __name__ == '__main__':
    squareList = main()
    print(f"Square of numbers: {squareList}")
    
    