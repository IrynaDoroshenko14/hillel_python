num_list = [2, 3, 7, 11, 56, 34, 89, 5, 44, 88]

count = 0
for i in range(len(num_list)):
    if num_list[i] % 2 == 1:
        num_list[i] = 0
        count += 1

print(num_list)
print(count)
