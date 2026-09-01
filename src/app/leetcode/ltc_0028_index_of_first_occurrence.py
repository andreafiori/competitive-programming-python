"""
Index of First Occurrence in a String | leetcode 28 | https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""

class IndexOfFirstOccurrence:

    def str_str(self, haystack: str, needle: str) -> int:
        ptr_l, ptr_r = 0, 0
        n_needle, n_haystack = len(needle), len(haystack)
        while ptr_r < n_haystack:
            if haystack[ptr_r] == needle[ptr_r - ptr_l]:
                ptr_r += 1
                if ptr_r - ptr_l > n_needle - 1:
                    return ptr_l
            else:
                ptr_r = ptr_l + 1
                ptr_l += 1
        return -1
