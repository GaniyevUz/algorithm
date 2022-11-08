# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        k = -1
        while n:
            if n & 1 == k:
                return False
            k = n & 1
            n >>= 1
        return True