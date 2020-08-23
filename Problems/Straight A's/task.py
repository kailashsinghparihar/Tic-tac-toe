# put your python code here
length = input()
leng = length.split()
le = []
for i in leng:
    if i == 'A':
        le.append(i)
ca = len(le) / (len(leng))
print(round(ca, 2))
