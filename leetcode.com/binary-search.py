# https://leetcode.com/problems/binary-search/

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

nums = [-1, 0, 3, 5, 9, 12]
target = 9
index = nums.index(target) if target in nums else -1
num = nums[:int(len(nums) / 2) - 1] if nums[int(len(nums) / 2)] < target else nums[int(len(nums) / 2) - 1:]
print(num)
for i, v in enumerate(nums):
    if v == target:
        print(i)
        break

# teacher's  example

from math import log2, ceil

arr = [2, 3, 4, 6, 7, 8, 9, 12, 13, 15, 16, 17, 18, 19]
x = 5

c = 0


# def binary_search(arr, l, r, x):
#     global c
#     c += 1
#     if r < l:
#         return -1
#     m = (l + r) // 2
#     if arr[m] == x:
#         return m
#     elif arr[m] < x:
#         return binary_search(arr, m + 1, r, x)
#     else:
#         return binary_search(arr, l, m - 1, x)

def binary_search_with_while(arr, l, r, x):
    result = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            result = m
            break
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return result


result = binary_search_with_while(arr, 0, len(arr) - 1, x)
print(result)

print(index)
