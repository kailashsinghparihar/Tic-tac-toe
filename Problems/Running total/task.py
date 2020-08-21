number = list(input())
old_list = [int(i) for i in number]
new_list = []
add = 0
for i in range(len(old_list)):
    if i >= 0:
        add += old_list[i]
        i -= 1
    new_list.append(add)
print(new_list)
