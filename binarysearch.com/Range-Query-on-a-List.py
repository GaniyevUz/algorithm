# https://binarysearch.com/problems/Range-Query-on-a-List

class RangeSum:

    def __init__(self, nums):
        self.rangelist = nums

    def total(self, i, j):
        return sum(self.rangelist[i:j])


r = RangeSum([1, 2, 5, 0, 3, 7])
print(r.total(0, 3))
print(r.total(1, 5))

