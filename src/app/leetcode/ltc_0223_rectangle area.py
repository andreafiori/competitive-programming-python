"""
Rectangle Area | https://leetcode.com/problems/rectangle-area/
"""
class RectangleArea:

    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # sum of areas of two rectangles
        result = (C - A) * (D - B) + (G - E) * (H - F)
        # no overlap
        if (C <= E or G <= A or H <= B or D <= F):
            return result
        # overlap length on x
        dx = min(C, G) - max(A, E)
        # overlap length on y
        dy = min(D, H) - max(B, F)
        return result - dx * dy
