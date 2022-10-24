a = [4, 3, 2, 7, 8, 1, 92, 32, 12, 54]

for i in range(1, len(a)):

    for j in range(i):
        if a[j] > a[i]:
            a[j], a[i] = a[i], a[j]
print('for based:', a)

i = 1
while i < len(a):
    j = i - 1
    while j > -1:
        if a[i] < a[j]:
            a[j], a[i] = a[i], a[j]
            i -= 1
        j -= 1
    i += 1

print('while based:', a)
