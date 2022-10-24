# https://binarysearch.com/problems/Detect-Voter-Fraud

class Solution:
    def solve(self, votes):
        return True if len({k: v for v, k in votes}) < len(votes) else False


votes = [
    [2, 3],
    [2, 2],
    [2, 1],
    [2, 0],
    [2, 1]
]
problem = Solution()
print(problem.solve(votes))
