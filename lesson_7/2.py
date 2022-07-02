input_temp = float(input("Enter temperature: "))
input_type = input("Enter type: ")


def calc_temp(temp, type_):
    if type_ == "C":
        celsius = temp
        fahrenheit = round((temp * 9/5) + 32, 2)
        kelvin = round(temp - 272.15, 2)
    elif type_ == "F":
        celsius = round((temp - 32) * 5/9, 2)
        fahrenheit = temp
        kelvin = round(celsius - 272.15, 2)
    elif type_ == "K":
        celsius = round(temp + 272.15, 2)
        fahrenheit = round((celsius * 9/5) + 32, 2)
        kelvin = temp
    else:
        return "Wrong type"

    return f"Input - {temp}, {type_}.\nCelsius - {celsius}, Fahrenheit - {fahrenheit}, Kelvin - {kelvin}"


print(calc_temp(input_temp, input_type))
