"""
337. House Robber III | https://leetcode.com/problems/house-robber-iii/



"""

from app.common.tree_node import TreeNode

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dic = {}
        return self._rob_helper(root, dic)

    # def rob_two(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     res = self._rob_helper(root: TreeNode)
    #     return max(res[0], res[1])

    def _rob_helper(self, root: TreeNode):
        if root is None:
            return [0, 0]
        left = self._rob_helper(root.left)
        right = self._rob_helper(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res

    # def _rob_helper(self, root: TreeNode, dic: dict) -> int:
    #     """
    #     Recursion with hash map
    #     :type root: TreeNode
    #     :type dic: dict
    #     :rtype: int
    #     """
    #     if root is None:
    #         return 0
    #     if root in dic:
    #         return dic[root]
    #     res = 0
    #     if root.left is not None:
    #         res += self._rob_helper(root.left.left, dic) + self._rob_helper(root.left.right, dic)
    #     if root.right is not None:
    #         res += self._rob_helper(root.right.left, dic) + self._rob_helper(root.right.right, dic)
    #     res =  max(res + root.val, self._rob_helper(root.left, dic) + self._rob_helper(root.right, dic))
    #     dic[root] = res
    #     return res