"""
Number of Segments in a String | leetcode 434 | https://leetcode.com/problems/number-of-segments-in-a-string/

"""

class NumberOfSegmentsInAString:

    def solution(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        segment_count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count