input_list_1 = [1, 2, 3, 4, 5]
input_list_2 = [3, 4, 5, 6, 7, 8]


def get_unique_nums(list_1, list_2):
    list_1.extend(list_2)
    set_ = set(list_1)
    return len(set_)


print(get_unique_nums(input_list_1, input_list_2))
