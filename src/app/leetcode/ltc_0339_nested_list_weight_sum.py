"""
Nested List Weight Sum | https://leetcode.com/problems/nested-list-weight-sum/
"""
class NestedInteger:

    def depth_sum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.depth_sum_helper(nestedList, 1)

    def depth_sum_helper(self, nestedList, depth):
        res = 0
        for l in nestedList:
            if l.isInteger():
                res += l.getInteger() * depth
            else:
                res += self.depth_sum_helper(l.getList(), depth + 1)
        return res
