num_list = []
while True:
    num = int(input("Please enter number: "))
    if num == 0:
        break
    elif num < 0:
        print("Please enter only positive numbers")
        continue
    num_list.append(num)

count = 0
for i in range(1, len(num_list)-1):
    if num_list[i] > num_list[i-1] and num_list[i] > num_list[i+1]:
        count += 1
print(count)


