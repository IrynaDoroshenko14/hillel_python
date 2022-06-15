horse_x = int(input("Please enter horse x coordinate: "))
horse_y = int(input("Please enter horse y coordinate: "))
x = int(input("Please enter expected x coordinate: "))
y = int(input("Please enter expected y coordinate: "))

delta_x = abs(horse_x - x)
delta_y = abs(horse_y - y)

if (delta_x == 2 and delta_y == 1) or (delta_x == 1 and delta_y == 2):
    print("YES")
else:
    print("NO")
