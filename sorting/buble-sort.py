a = [4, 3, 2, 7, 8, 1, 92, 32, 12, 54]
for i in range(len(a)):
    for j in range(1, len(a) - i):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
print(a)
