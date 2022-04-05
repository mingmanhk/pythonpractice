from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(root: Optional[TreeNode]) -> bool:
        def valid(node, left= - math.inf, right= math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high
            if node.val<=left or node.val>=right:
                return False
            # The left and right subtree must also be valid.
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
            return valid(root)

    print(isValidBST([1,2,3]))