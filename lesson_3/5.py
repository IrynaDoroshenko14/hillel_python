from random import randrange

for _ in range(3):
    num = randrange(1, 11)
    user_num = int(input("Please enter num: "))

    if num == user_num:
        print("You won!")
    else:
        print("You lose!")
