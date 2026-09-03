"""
Binary tree paths | leetcode 257 | https://leetcode.com/problems/binary-tree-paths/

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

"""

from typing import Optional, List

from app.common.tree_node import TreeNode

class BinaryTreePath:

    def solution(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        paths = []
        self._get_path(paths, [], root)
        res = ['->'.join(p) for p in paths ]
        return res

    def _get_path(self, result: List[List[str]], path: List[str], node: TreeNode):
        if node.left is None and node.right is None:
            result.append(path + [str(node.val)])
            return
        path = path + [str(node.val)]
        if node.left is not None:
            self._get_path(result, path, node.left)
        if node.right is not None:
            self._get_path(result, path, node.right)
