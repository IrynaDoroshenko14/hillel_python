first_list = [3, 5, 7, 1, 2, 9]
second_list = [4, 5, 9, 1, 2, 0]

in_both = []
only_first = []
unique = []
# числа, що містяться одночасно як у першому списку, так і в другому
for num_1 in first_list:
    for num_2 in second_list:
        if num_1 == num_2:
            in_both.append(num_1)
print(in_both)
# числа, що містяться в першому, але відсутні в другому
for num_1 in first_list:
    if num_1 not in second_list:
        only_first.append(num_1)
print(only_first)
# тільки унікальні для першого та другого списків
for num_1 in first_list:
    if num_1 not in second_list:
        unique.append(num_1)
for num_2 in second_list:
    if num_2 not in first_list:
        unique.append(num_2)
print(unique)
