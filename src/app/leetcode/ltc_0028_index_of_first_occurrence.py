import re

"""
Index of First Occurrence in a String | https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
class IndexOfFirstOccurrence:

    def find_regex(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        match = re.search(needle, haystack)
        return match.start() if match else -1

    def find_sliding(self, haystack: str, needle: str) -> int:
        ptrL, ptrR = 0, 0
        N_needle, N_haystack = len(needle), len(haystack)
        while ptrR < N_haystack:
            if haystack[ptrR] == needle[ptrR - ptrL]:
                ptrR += 1
                if ptrR - ptrL > N_needle - 1:
                    return ptrL
            else:
                ptrR = ptrL + 1
                ptrL += 1
        return -1
