"""
Implement strStr() | https://leetcode.com/problems/implement-strstr/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
    What should we return when needle is an empty string? This is a great question to ask during an interview.


"""
class ImplementStrStr:
    def solution_one(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

    # def solution_one(self, haystack, needle):
    #     lsh, lsn = len(haystack), len(needle)
    #     if lsn == 0:
    #         return 0
    #     pos, index = 0, 0
    #     while index <= lsh - lsn:
    #         if haystack[index] == needle[0]:
    #             # slice index:index + lsn
    #             if haystack[index:index + lsn] == needle:
    #                 return index
    #         index += 1
    #     return -1

    def solution_two(self, haystack, needle):
        lsh, lsn = len(haystack), len(needle)
        if lsn == 0:
            return 0
        next = self.makeNext(needle)
        i = j = 0
        while i < lsh:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == lsn:
                    return i - lsn
            if i < lsh and haystack[i] != needle[j]:
                j = next[j]
        return -1

    def make_next(self, needle):
        ls = len(needle)
        next = [0] * ls
        next[0], i, j = -1, 0, -1
        while i < ls - 1:
            if j == -1 or needle[i] == needle[j]:
                next[i + 1] = j + 1
                if needle[i + 1] == needle[j + 1]:
                    next[i + 1] = next[j + 1]
                i += 1
                j += 1
            if needle[i] != needle[j]:
                j = next[j]
        return next
