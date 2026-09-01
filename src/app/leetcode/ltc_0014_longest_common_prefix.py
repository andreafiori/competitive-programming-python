"""
Longest Common Prefix | leetcode 14 | https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

"""

from typing import List

class LongestCommonPrefix:
    def find(self, strs: List[str]) -> str:
        ls = len(strs)
        if ls == 1:
            return strs[0]
        prefix = ''
        pos = 0
        while True:
            try:
                current = strs[0][pos]
            except IndexError:
                break
            index = 1
            while index < ls:
                try:
                    if strs[index][pos] != current:
                        break
                except IndexError:
                    break
                index += 1
            if index == ls:
                prefix = prefix + current
            else:
                break
            pos += 1
        return prefix

    def find3(self, strs: List[str]) -> str:
        res = ""
        n = len(strs)
        strs.sort()
        first = strs[0]
        last = strs[n - 1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return res
            else:
                res = res + first[i]
        return res
