"""
Shortest Word Distance | https://leetcode.com/problems/shortest-word-distance/
"""
class ShortestWordDistance:

    def find_shortest_distance(self, words: list[str], word1: str, word2: str) -> int:
        index1 = index2 = -1
        res = len(words)
        for index, word in enumerate(words):
            if word1 == word:
                index1 = index
            elif word2 == word:
                index2 = index
            if index1 != -1 and index2 != -1:
                res = min(res, abs(index1 - index2))
        return res
