# https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0].isdigit():
            x = ''.join([i for i in x[::-1]])
        else:
            x = x[0] + ''.join([i for i in x[1:len(x)][::-1]])
        if -2147483648 > int(x) or int(x) > 2147483647:
            return 0
        return int(x)
