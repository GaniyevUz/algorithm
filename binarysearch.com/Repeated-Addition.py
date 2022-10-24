# https://binarysearch.com/problems/Repeated-Addition


class Solution:
    def solve(self, n):
        nums = sum(map(int, str(n)))
        n = 0
        for i in str(nums):
            n += int(i)
        return n

n = 8835
problem = Solution()
print(problem.solve(n))
