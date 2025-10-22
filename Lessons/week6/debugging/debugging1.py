def convert_to_fahrenheit(celsius:int):
    fah1 = (celsius * 9)
    fah2 = (fah1 + 32)/5
    return fah2

temp = int(input("Enter temperature in Celsius: "))
fahrenheit = convert_to_fahrenheit(temp)
print("Temperature in Fahrenheit is ", fahrenheit)
print("Conversion complete!")

if fahrenheit > 100:
    print("That's boiling point!")
convert_to_fahrenheit(13)