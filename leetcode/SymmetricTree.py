from typing import Optional
import math
from xml.etree.ElementTree import TreeBuilder

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.isSymmetricRec(root.left, root.right)

    def isSymmetricRec(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRec(left.left, right.right) and self.isSymmetricRec(left.right, right.left)
        