# https://leetcode.com/problems/single-number-ii/

from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i, v in Counter(nums).items():
            if v == 1:
                return i