a = [4, 3, 2, 7, 8, 1, 92, 32, 12, 54]
n = 3
for i, v in enumerate(a):
    if v == n:
        print('Found at', i)
        break
else:
    print('Not Found')
