# https://leetcode.com/problems/peak-index-in-a-mountain-array/
from typing import List

arr = [0, 10, 5, 2]


# def peakIndexInMountainArray(arr: List[int]) -> int:
#     if len()
#    return


print(sorted(enumerate(arr), key=lambda x: x[1], reverse=True)[0][0])
