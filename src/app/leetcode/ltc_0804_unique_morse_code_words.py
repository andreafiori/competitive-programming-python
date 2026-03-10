"""
Unique Morse Code Words | https://leetcode.com/problems/unique-morse-code-words/

https://leetcode.com/problems/unique-morse-code-words/solution/
"""
class UniqueMorseCodeWords:

    def __init__(self):
        self.morse_tab = [".-","-...","-.-.",
            "-..",".","..-.","--.","....",
            "..",".---","-.-",".-..","--",
            "-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--",
            "-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0:
            return 0
        ans_set = set()
        for word in words:
            morsed = ""
            for c in word:
                morsed +=self.morse_tab[ord(c) - ord('a')]
            ans_set.add(morsed)
        return len(ans_set)
