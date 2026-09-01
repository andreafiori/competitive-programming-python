"""
Construct Binary Tree from Preorder and Inorder Traversal | Leetcode 105 | Medium | https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ConstructBinaryTreeFromPreorderAndInorderTraversal:
    def buildTree(self, preorder, inorder):
        n = len(inorder)
        inOrderMap = {inorder[i]: i for i in range(n)}
        return self.buildTreeUtil(preorder, inorder, inOrderMap, 0, n - 1, 0, n - 1)

    def buildTreeUtil(self, preorder, inorder, inOrderMap, pStart, pEnd, iStart, iEnd):
        if pStart > pEnd or iStart > iEnd:
            return None
        root = TreeNode(preorder[pStart])
        rootIdx = inOrderMap[root.val]
        root.left = self.buildTreeUtil(preorder, inorder, inOrderMap, pStart + 1, pStart + rootIdx - iStart + 1, iStart, rootIdx - 1)
        root.right = self.buildTreeUtil(preorder, inorder, inOrderMap, pStart + rootIdx - iStart + 1, pEnd, rootIdx + 1,
                                        iEnd)
        return root
