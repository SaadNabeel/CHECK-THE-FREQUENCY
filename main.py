d = {'a': 2, 'b': 3, 'c': 2, 'e': 3, 'f': 2}

count = 0


for c in d.values():
    if c == 2: 
        count += 1


print('Frequency of 2:', count)
