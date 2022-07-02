input_list = ['a', 'b', 'c', 'd', 'e']


def create_num_dict(list_):
    output_dict = {}
    for num, value in zip(range(len(list_)), list_):
        output_dict[num] = value
    return output_dict


print(create_num_dict(input_list))
