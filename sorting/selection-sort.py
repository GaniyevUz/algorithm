a = [2, 6, 3, 7, 5, 2, 4]

# for i in range(len(a)):
#     minimum = i
#     for j in range(i + 1, len(a)):
#         if a[minimum] > a[j]:
#             minimum = j
#     a[i], a[minimum] = a[minimum], a[i]
#
# print(a)

i = 0
while i < len(a):
    j = i + 1
    minimum = i
    while j < len(a):
        if a[minimum] > a[j]:
            minimum = j
        j += 1
    a[i], a[minimum] = a[minimum], a[i]
    i += 1

print(a)
