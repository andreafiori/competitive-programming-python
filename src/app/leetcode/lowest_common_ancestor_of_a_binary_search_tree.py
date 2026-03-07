from common.tree_node import TreeNode

class LowestCommonAncestorOfABinarySearchTree:

    def find(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # use the BST to reduce the search space
        if p is None or q is None or root is None:
            return None
        if p.val < root.val and q.val < root.val:
            return self.find(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.find(root.right, p, q)
        else:
            return root
