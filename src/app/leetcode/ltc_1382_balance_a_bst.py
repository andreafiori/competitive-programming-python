# balance a bst | leetcode 1382 | https://leetcode.com/problems/balance-a-binary-search-tree/
# given a bst, return a balanced bst
# method: use inorder traversal to make a sorted array, convert sorted array to balanced bst

from common.tree_node import TreeNode

class BalanceBST:
    # convert sorted array to bst
    def sorted_array_to_BST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(val = nums[mid])
        root.left = self.sorted_array_to_BST(nums[:mid])
        root.right = self.sorted_array_to_BST(nums[mid+1:])

        return root

    # in-order traveral gives sorted array
    def inorder_traversal(self, root):
        travList = []

        self.traverse(root, travList)
        return travList

    def traverse(self, root, travList):
        if root is None:
            return None

        self.traverse(root.left, travList)
        travList.append(root.val)
        self.traverse(root.right, travList)

    def balance_BST(self, root):
        """ Balance a binary search tree """
        return self.sorted_array_to_BST(self.inorder_traversal(root))