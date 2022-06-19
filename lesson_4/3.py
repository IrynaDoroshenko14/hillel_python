a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))

if a < b:
    print(*list(range(a, b + 1)))
else:
    print(*list(range(a, b - 1, -1)))