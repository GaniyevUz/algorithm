# https://binarysearch.com/problems/K-Longest-Show-Durations

class Solution:
    def solve(self, shows, durations, k):
        t = dict()
        for i, v in zip(shows, durations):
            t[i] = v + t.get(i, 0)
        return sum(sorted(t.values(), reverse=True)[:k])


shows = ["Top Gun", "Aviator", "Top Gun", "Roma", "Logan"]
durations = [5, 3, 5, 13, 4]
k = 2

problem = Solution()
print(problem.solve(shows, durations, k))
