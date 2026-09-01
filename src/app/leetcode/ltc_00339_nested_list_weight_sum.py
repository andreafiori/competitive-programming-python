"""
Nested List Weight Sum | leetcode 339 | https://leetcode.com/problems/nested-list-weight-sum/

"""

class NestedListWeightSum:

    def depth_sum(self, nested_list):
        """
        :type nested_list: List[NestedInteger]
        :rtype: int
        """
        return self.depth_sum_helper(nested_list, 1)

    def depth_sum_helper(self, nested_list, depth):
        res = 0
        for l in nested_list:
            if l.isInteger():
                res += l.getInteger() * depth
            else:
                res += self.depth_sum_helper(l.getList(), depth + 1)
        return res
