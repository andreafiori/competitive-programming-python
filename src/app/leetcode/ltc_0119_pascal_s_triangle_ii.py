"""
Pascal's Triangle II | leetcode 119 | https://leetcode.com/problems/pascals-triangle-ii/

"""

class PascalTriangleII:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        last = [1]
        res = [1]
        for r in range(1, rowIndex + 1):
            res = [1]
            for index in range(len(last) - 1):
                res.append(last[index] + last[index + 1])
            res.append(1)
            last = res
        return res
