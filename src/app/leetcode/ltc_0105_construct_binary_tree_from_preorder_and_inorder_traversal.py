from common.tree_node import TreeNode

"""
Construct Binary Tree from Preorder and Inorder Traversal | https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
class ConstructBinaryTreeFromPreorderAndInorderTraversal:

    def build_tree(self, preorder, inorder):
        n = len(inorder)
        inOrderMap = {inorder[i]: i for i in range(n)}
        return self._build_tree_util(preorder, inorder, inOrderMap, 0, n - 1, 0, n - 1)

    def _build_tree_util(self, preorder, inorder, inOrderMap, pStart, pEnd, iStart, iEnd):
        if pStart > pEnd or iStart > iEnd:
            return None
        root = TreeNode(preorder[pStart])
        rootIdx = inOrderMap[root.val]
        root.left = self._build_tree_util(preorder, inorder, inOrderMap, pStart + 1, pStart + rootIdx - iStart + 1, iStart, rootIdx - 1)
        root.right = self._build_tree_util(preorder, inorder, inOrderMap, pStart + rootIdx - iStart + 1, pEnd, rootIdx + 1,
                                        iEnd)
        return root
