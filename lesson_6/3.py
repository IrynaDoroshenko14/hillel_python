input_list = ['a', 'b', 'c', 'd', 'e']

output_dict = {}
for num, value in zip(range(len(input_list)), input_list):
    output_dict[num] = value

print(output_dict)
