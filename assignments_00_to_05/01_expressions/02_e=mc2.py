c: int = 299792458  # The speed of light in m/s

def main():
    mass=float(input("Enter mass in kilograms(65.8): "))
    energy  =mass*c**2
    print("e=m*c**2")
    print(f"m = {mass}kg")
    print(f"c = {c}m/s")
    print(f"Energy after calculation is {energy:.3e} joules of energy")
    

if __name__ == '__main__':
    main()
    