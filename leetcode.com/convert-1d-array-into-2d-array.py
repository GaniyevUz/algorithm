# https://leetcode.com/problems/convert-1d-array-into-2d-array/


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        result = []
        for i in range(m):
            for j in range(n):
                if original:
                    result.append(original[:n])
                    original = original[n:]
        return result
