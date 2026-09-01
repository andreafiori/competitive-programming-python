"""
Minimum Increment to Make Array Unique | leetcode 945 | https://leetcode.com/problems/minimum-increment-to-make-array-unique/
"""

class MinIncrementToMakeArrayUnique:

    def solution(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        if a is None or len(a) == 0:
            return 0
        res = 0
        num_set = set()
        duplicate = []
        a.sort()
        left, right = a[0], a[-1]
        holes = right - left + 1
        for v in a:
            if v in num_set:
                duplicate.append(v)
            else:
                num_set.add(v)
        holes = holes - len(num_set)
        # find a hole for these math
        for hole in range(left + 1, right):
            if holes == 0 or len(duplicate) == 0:
                break
            if hole not in num_set and hole > duplicate[0]:
                res += hole - duplicate.pop(0)
                holes -= 1
        while len(duplicate) != 0:
            right += 1
            res += right - duplicate.pop(0)
        return res
