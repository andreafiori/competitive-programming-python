"""
. Poor Pigs | https://leetcode.com/problems/poor-pigs/
"""
class PoorPigs(object):
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
