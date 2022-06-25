from math import sqrt

a = int(input("Please enter number: "))


def square(length):
    perimeter = 4*length
    square_ = length**2
    diagonal = length*sqrt(2)
    return perimeter, square_, diagonal


print(square(a))
