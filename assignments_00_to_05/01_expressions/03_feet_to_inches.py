# Convert feet to inches

inchesInFoot:int=12
def main():
    feet:float=float(input("Enter number of feet: "))
    convertToInches:float = feet*inchesInFoot
    print(f"{feet} feet = {convertToInches:.2f} inches")
    
    
if __name__ == '__main__':
    main()
    