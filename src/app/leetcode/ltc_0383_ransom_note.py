"""
Leetcode Problem: Ransom Note | https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letter_map = {}
        for letter in magazine:
            letter_map[letter] = letter_map.get(letter, 0) + 1
        for letter in ransomNote:
            letter_map[letter] = letter_map.get(letter, 0) - 1
            if letter_map[letter] < 0:
                return False
        return True

    # def canConstruct(self, ransomNote, magazine):
    #     return not collections.Counter(ransomNote) - collections.Counter(magazine)
