def temperature_converter():
    temperature = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

    if unit == 'C':
        converted_temp = (temperature * 9/5) + 32
        print("Converted temperature:", converted_temp, "F")
    elif unit == 'F':
        converted_temp = (temperature - 32) * 5/9
        print("Converted temperature:", converted_temp, "C")
    else:
        print("Invalid unit")

temperature_converter()
