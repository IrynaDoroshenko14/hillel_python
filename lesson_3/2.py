num = input("Please enter float number: ")
fract = num.split(".")[1]
first_digit = fract[0]
print(f"Number {num} has a fractional part {fract}")
print(f"First digit of {fract} is {first_digit}")