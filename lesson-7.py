from collections import Counter
from typing import List


# nums = [0, 1, 2]
# even = []
# odd = []
# for i in nums:
#     if i & 1:
#         odd.append(i)
#     else:
#         even.append(i)

# print(even + odd)


# l = 0
# r = len(nums) - 1
# while l < r:
#     if not nums[l] & 1:
#         l += 1
#     elif nums[r] & 1:
#         r -= 1
#     else:
#         nums[l], nums[r] = nums[r], nums[l]
#         l += 1
#         r -= 1

# nums = [-4, -1, 0, 3, 10]
# l, r = 0, 0
#
# while l < r:
#     if abs(nums[l]) > abs(nums[r]):
#         nums[l] *= nums[l]
#         l += 1
#     elif nums[l] < nums[r]:
#         r += 1
#     else:
#
#         l += 1
#         r -= 1
# print(nums)

# def restoreString(s: str, indices: List[int]) -> str:
#     d = {}
#     for i in range(len(indices)):
#         d[indices[i]] = s[i]
#     return ''.join(v for i, v in sorted(d.items()))
#
#
# s = "codeleet"
# indices = [4, 5, 6, 7, 0, 2, 1, 3]
# print(restoreString(s, indices))

def isHappy(n: int) -> bool:

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

n = 2

print(isHappy(n))
