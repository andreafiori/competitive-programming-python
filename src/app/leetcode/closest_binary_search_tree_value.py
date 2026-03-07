"""
Closest Binary Search Tree Value | https://leetcode.com/problems/closest-binary-search-tree-value/

"""

class ClosestBinarySearchTreeValue:
    def closest_value(self, root, target):
        kid = root.left if target < root.val else root.right
        if not kid:
            return root.val
        kid_min = self.closest_value(kid, target)
        return min((kid_min, root.val), key=lambda x: abs(target - x))
