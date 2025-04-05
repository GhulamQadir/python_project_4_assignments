def main():
    firstNum:int=int(input("Please enter an integer to be divided: "))
    secondNum:int=int(input("Please enter an integer to be divide by: "))
    
    quotient:int = firstNum//secondNum
    remainder:int= firstNum%secondNum
    print(f"The result of this division is {quotient} with a remainder of {remainder}")
    
    
if __name__ == '__main__':
    main()