words = input()
wo = words.split()
word = []
for i in wo:
    if i.endswith('s'):
        word.append(i)
print('_'.join(word))
