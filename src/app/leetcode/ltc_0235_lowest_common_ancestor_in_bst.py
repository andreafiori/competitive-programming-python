"""

lowest common ancestor in binary search tree | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Method: iteration through each node, when p and q are in different subtrees, current node is LCA

"""

from common.tree_node import TreeNode

class LowestCommonAncestor:
    def find(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

        return root
