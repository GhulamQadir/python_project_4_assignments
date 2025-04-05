import math
def main():
    side1:float = float(input("Enter the length of AB: "))
    side2:float = float(input("Enter the length of AC: "))
    calcLength:float = math.sqrt(side1**2 + side2**2)
    print(f"The length of BC (the hypotenuse) is: {calcLength}")
    
if __name__ == '__main__':
    main()
        