from common.tree_node import TreeNode

class SecondMinimumNodeInABinaryTree:

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        ans = float('inf')
        min_val = root.val
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if min_val < curr.val < ans:
                ans = curr.val
            elif curr.val == min_val:
                stack.append(curr.left)
                stack.append(curr.right)
        return ans if ans < float('inf') else -1
