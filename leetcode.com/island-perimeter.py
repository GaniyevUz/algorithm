# https://leetcode.com/problems/island-perimeter
from typing import List


# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


class Solution:
    def islandPerimeter(self, a: List[List[int]]) -> int:
        res = 0
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 1:
                    res += 4
                    if i > 0 and a[i - 1][j] == 1:
                        res -= 2
                    if j > 0 and a[i][j - 1] == 1:
                        res -= 2
        return res