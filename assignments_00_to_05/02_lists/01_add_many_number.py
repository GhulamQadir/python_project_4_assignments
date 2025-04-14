def main(numList:int)->int:
    sum:int = 0
    for i in numList:
        sum+=i
    return sum        
    
    
if __name__ == '__main__':
    numList:list[int]= [2,5,3,5,7]
    sumOfNums = main(numList)
    print(f"Sum of number is {sumOfNums}")