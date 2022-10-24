# d = {len(i): i for i in input().split()}
# print(d[max(d)])

# https://algo.ubtuit.uz/problem/164

# s = input()
# l, r = map(int, input().split())
# if l > r:
#     print(s[r-1:l][::-1])
# else:
#     print(s[l - 1:r])

# from math import sin
#
# t, s = map(float, input().split())
#
#
# def f(a, b, c):
#     return (2 * a - b - sin(c)) / (5 + abs(c))
#
#
# r = f(t, -2 * s, 1.17) + f(2.2, t, s - t)
# print(f"{r:.2f}")

# https://algo.ubtuit.uz/problem/175

# s = input()
# temp = ''
#
# for i in s:
#     if i == '(' or '(' in temp:
#         temp += i
#     if i == ')':
#         s = s.replace(temp, temp[1:-1][::-1])
#         temp = ''
#
# print(s)
# n = set(map(int, input().split()))
#
# while n != '{0}':
#     if len(n) == 3:
#         print("yes")
#     else:
#         print("no")
#     n = set(map(int, input().split()))