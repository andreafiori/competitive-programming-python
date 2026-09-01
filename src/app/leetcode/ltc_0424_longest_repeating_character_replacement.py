"""

Longest repeating character replacement | leetcode 424 | https://leetcode.com/problems/longest-repeating-character-replacement/

Keep track of max freq in sliding window and check if size of window - max freq > k

"""

class LongestRepeatingCharacterReplacement:
    def solution(self, s: str, k: int) -> int:
        ptr_l = 0
        ptr_r = 0
        longest = 0
        freq = dict()
        max_freq = 0

        for ptr_r in range(len(s)):
            freq[s[ptr_r]] = 1 + freq.get(s[ptr_r], 0)
            max_freq = max(max_freq, freq[s[ptr_r]])

            if (ptr_r - ptr_l + 1) - max_freq > k:
                freq[s[ptr_l]] -= 1
                ptr_l += 1

            longest = max(longest, (ptr_r - ptr_l + 1))

        return longest