num = int(input())
value_list = []
for i in range(num):
    value = input()
    if value.endswith('win'):
        du = value.replace('win', '')
        value_list.append(du.strip())
print(value_list)
print(len(value_list))
