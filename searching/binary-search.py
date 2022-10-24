a = [1, 2, 3, 4, 7, 8, 12, 32, 54, 92]
n = 3
l, r = 0, len(a) - 1

while l < r:
    m = (l + r) // 2
    if a[m] == n:
        print('Found at', m)
        break
    elif a[m] < n:
        l = m + 1
    else:
        r = m - 1
else:
    print('Not Found')
