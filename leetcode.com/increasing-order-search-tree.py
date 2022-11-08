# https://leetcode.com/problems/increasing-order-search-tree/

# Given the root of a binary search tree, rearrange the tree in in-order
# so that the leftmost node in the tree is now the root of the tree,
# and every node has no left child and only one right child.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def add(root, n):
    if not root:
        return TreeNode(n)
    if root.val > n:
        root.left = add(root.left, n)
    else:
        root.right = add(root.right, n)
    return root


l = [5, 3, 6, 2, 4, 8, 1, 7, 9]
root = TreeNode(25)
for i in l:
    add(root, i)


class Solution:
    def in_order(self, root):
        if not root:
            return []
        return self.in_order(root.left) + [root.val] + self.in_order(root.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return TreeNode()
        return self.increasingBST(TreeNode(root.right))


problem = Solution()
print(problem.in_order(root))
print(problem.increasingBST(root))