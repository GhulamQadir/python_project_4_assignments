numOfDays:int=365
numOfHours:int=24
numOfMinutes:int=60
numOfSeconds:int=60


def main():
    calcSeconds:int=numOfDays*numOfHours*numOfMinutes*numOfSeconds
    print(f"There are {calcSeconds} in a year")
    
    
if __name__ == '__main__':
    main()