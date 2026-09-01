"""
Leetcode Problem 804: Unique Morse Code Words | https://leetcode.com/problems/unique-morse-code-words/
"""
class UniqueMorseCodeWords:

    morse_tab = [".-","-...","-.-.",
                "-..",".","..-.","--.","....",
                "..",".---","-.-",".-..","--",
                "-.","---",".--.","--.-",".-.",
                "...","-","..-","...-",".--",
                "-..-","-.--","--.."]

    def solution(self, words: list[str]) -> int:
        """
        :param words: list[str]
        :return: int
        """
        if len(words) == 0:
            return 0
        ans_set = set()
        for word in words:
            morsed = ""
            for c in word:
                morsed += self.morse_tab[ord(c) - ord('a')]
            ans_set.add(morsed)
        return len(ans_set)
