def main():
    tempInFahrenheit:float = float(input("Enter temperature in Fahrenheit:\t"))
    convertToCelsius:float = round(((tempInFahrenheit-32)*5.0/9.0),4)
    print(f"Temperature: {tempInFahrenheit}F = {convertToCelsius}C")
    


if __name__ == '__main__':
    main()    
    