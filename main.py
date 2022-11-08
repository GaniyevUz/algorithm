from typing import List

#
# list1 = ["Shogun", "Piatti", "Tapioca Express", "Burger King", "KFC"]
#
# list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
#
#
# def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
#     l1 = {v: i for i, v in enumerate(list1)}
#     d = {}
#     l = []
#     for i, v in enumerate(list2):
#         if v in l1.keys():
#             d[v] = sum((l1[v], i))
#     min_ = min(d.values())
#     for i, v in d.items():
#         if v == min_:
#             l.append(i)
#     return l
#
#
# print(findRestaurant(list1, list2))


# a = [
#     [9, 9, 8, 1],
#     [5, 6, 11, 6],
#     [8, 2, 6, 4],
#     [6, 2, 2, 2]
# ]
#
# result = [[max(a[i - 1][j - 1:j + 2] + a[i][j - 1:j + 2] + a[i + 1][j - 1:j + 2]) for j in range(1, len(a) - 1)] for i in range(1, len(a) - 1)]
# print(result)

# https://leetcode.com/problems/flipping-an-image/submissions/
# image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
# print(list([1 if j == 0 else 0 for j in i[::-1]] for i in image))

matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]

for i in range(1, len(matrix)):
    for j in range(1, len(matrix[i])):
        if matrix[i][j] == matrix[i - 1][j - 1]:
            print(matrix[i][j], end=' ')
    print()
