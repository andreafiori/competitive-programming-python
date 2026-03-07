"""
Verifying an Alien Dictionary | https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
    

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.

"""

class VerifyingAnAlienDictionary:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = {}
        for i, v in enumerate(order):
            order_map[v] = i

        def cmp_alien(x, y):
            ls = min(len(x), len(y))
            index = 0
            while index < ls:
                if x[index] != y[index]:
                    return order_map[x[index]] - order_map[y[index]]
                index += 1
            return len(x) - len(y)
        pos = 0
        while pos + 1 < len(words):
            if cmp_alien(words[pos], words[pos + 1]) > 0:
                return False
            pos += 1
        return True
