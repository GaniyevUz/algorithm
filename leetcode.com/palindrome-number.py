# https://leetcode.com/problems/palindrome-number
# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
# For example, 121 is a palindrome while 123 is not.

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l, r = 0, len(x) - 1
        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True
        # return True if str(x)[::-1] == str(x) else False


x = 121
problem = Solution()
print(problem.isPalindrome(x))
