"""
Palindrome Permutation | https://leetcode.com/problems/palindrome-permutation/
"""
class PalindromePermutation:
    """Palindrome Permutation implementation"""

    def canPermutePalindrome(self, s: str) -> bool:
        """
        :param s: str
        :return: bool
        """
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        odd, even = 0, 0
        for c in dic:
            if dic[c] % 2 == 0:
                even += 1
            else:
                odd += 1
        if odd <= 1:
            return True
        return False
