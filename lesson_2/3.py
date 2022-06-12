v = int(input("Please enter speed: "))
t = int(input("Please enter time: "))

if v < 0:
    v = 0
distance = v*t

print(f"Vasya has rode {distance}")
