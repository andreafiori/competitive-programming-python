from common.tree_node import TreeNode

"""
Unique Binary Search Trees II | https://leetcode.com/problems/unique-binary-search-trees-ii/
"""
class UniqueBinarySearchTreesII:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.get_trees(1, n)

    def get_trees(self, start: int, end: int) -> list[TreeNode]:
        """ Recursive solve this problem """
        res = []
        if start > end:
            res.append(None)
            return res
        for i in range(start, end + 1):
            lefts = self.get_trees(start, i - 1)
            rights = self.get_trees(i + 1, end)
            for j in range(len(lefts)):
                for k in range(len(rights)):
                    # root point
                    root = TreeNode(i)
                    root.left = lefts[j]
                    root.right = rights[k]
                    res.append(root)
        return res
