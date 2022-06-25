def get_square(a, b, figure="triangle"):
    if figure == "triangle":
        return a * b / 2
    elif figure == "rectangle":
        return a * b
