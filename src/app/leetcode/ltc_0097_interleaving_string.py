"""
Interleaving String | https://leetcode.com/problems/interleaving-string/

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
    Explanation: One way to obtain s3 is:
    Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
    Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
    Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false
    Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
    Input: s1 = "", s2 = "", s3 = ""
    Output: true

Constraints:
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.

"""

class InterleavingString:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        queue = [(0, 0), (-1, -1)]
        visited = set()
        isSuccess = False
        index = 0
        while len(queue) != 1 or queue[0][0] != -1:
            p = queue.pop(0)
            if p[0] == len(s1) and p[1] == len(s2):
                return True
            if p[0] == -1:
                queue.append(p)
                index += 1
                continue
            if p in visited:
                continue
            visited.add(p)
            if p[0] < len(s1):
                if s1[p[0]] == s3[index]:
                    queue.append((p[0] + 1, p[1]))
            if p[1] < len(s2):
                if s2[p[1]] == s3[index]:
                    queue.append((p[0], p[1] + 1))
        return False
