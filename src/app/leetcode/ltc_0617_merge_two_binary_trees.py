"""
Merge Two Binary Trees | LeetCode 617 | https://leetcode.com/problems/merge-two-binary-trees/

"""

from src.app.leetcode.tree_node import TreeNode

class MergeTwoBinaryTrees:

    def solution(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        :param t1: TreeNode
        :param t2: TreeNode
        :return: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.solution(t1.left, t2.left)
        t1.right = self.solution(t1.right, t2.right)
        return t1

    # def mergeTrees(self, t1, t2):
    #     if t1 is None:
    #         return t2
    #     stack = [(t1, t2)]
    #     while len(stack) != 0:
    #         n1, n2 = stack.pop()
    #         if n1 is None or n2 is None:
    #             continue
    #         n1.val += n2.val
    #         if n1.left is None:
    #             n1.left = n2.left
    #         else:
    #             stack.insert(0, (n1.left, n2.left))
    #         if n1.right is None:
    #             n1.right = n2.right
    #         else:
    #             stack.insert(0, (n1.right, n2.right))
    #     return t1
