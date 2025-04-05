import random

numOfSides=6

def main():
    die1:int=random.randint(1,numOfSides)
    die2:int=random.randint(1,numOfSides)
    total:int = die1+die2
    
    # Print out the results
    print("Dice have", numOfSides, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)
    

if __name__ == '__main__':
    main()