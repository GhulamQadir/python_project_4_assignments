import random

"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

dieSides:int=6
def rollDice():
    die1:int=random.randint(1,dieSides)
    die2:int=random.randint(1,dieSides)
    totalOfDice:int = die1+die2
    print("Total of two dice:", totalOfDice)

    
def main():
    die1:int =12    
    """scope of variable: its scope is within the main function so the value of die1 within
    rollDice function will not be affected"""
    print(f"die1 in main() starts as {die1}")
    rollDice()
    rollDice()
    rollDice()
    print(f"die1 in main() is: {die1}")


if __name__ == '__main__':
    main()