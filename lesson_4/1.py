x = int(input("Please enter first day' distance: "))
y = int(input("Please enter expected distance: "))

day = 1
while x < y:
    day += 1
    x *= 1.1

print(day)
