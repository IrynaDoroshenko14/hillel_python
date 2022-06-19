def mul(number_list):
    result = 1
    for number in number_list:
        result *= number
    return result


def average(number_list):
    return sum(number_list)/len(number_list)


def biggest_count(number_list):
    count = 0
    big = biggest(number_list)[0]
    for number in number_list:
        if number == big:
            count += 1
    return count


def biggest(number_list):
    big = number_list[0]
    el_num = 0
    for enum, number in enumerate(number_list):
        if number > big:
            big = number
            el_num = enum
    return big, el_num


def even(number_list):
    count = 0
    for number in number_list:
        if number % 2 == 0:
            count += 1
    return count


def odd(number_list):
    count = 0
    for number in number_list:
        if number % 2 == 1:
            count += 1
    return count


def second_biggest(number_list):
    return sorted(number_list)[-2]

num_list = []
while True:
    num = int(input("Please enter number: "))
    if num == 0:
        break
    elif num < 0:
        print("Please enter only positive numbers")
        continue
    num_list.append(num)

# кількість введених чисел (завершальний 0 не рахується)
print(len(num_list))
# їхню суму
print(sum(num_list))
# добуток
print(mul(num_list))
# середнє арифметичне (крім завершального числа 0)
print(average(num_list))
# Визначити значення та порядковий номер найбільшого елемента послідовності
print(biggest(num_list))
# визначити кількість парних та непарних елементів у послідовності
print(even(num_list), odd(num_list))
# Визначити значення другого за величиною елемента в цій послідовності
print(second_biggest(num_list))
# визначте, скільки елементів цієї послідовності дорівнюють її найбільшому елементу
print(biggest_count(num_list))