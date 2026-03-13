"""
One Edit Distance | https://leetcode.com/problems/one-edit-distance/
"""
class OneEditDistance(object):

    def is_one_edit_distance(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls_s, ls_t = len(s) ,len(t)
        # reverse to reduce conditions
        if ls_s > ls_t:
            return self.is_one_edit_distance(t, s)
        # edit distance is greater than 1
        if ls_t - ls_s > 1:
            return False
        i, shift = 0, ls_t - ls_s
        # find the different position
        while i < ls_s and s[i] == t[i]:
            i += 1
        if i == ls_s:
            return shift > 0
        if shift == 0:
            i += 1
        while i < ls_s and s[i] == t[i + shift]:
            i += 1
        return i == ls_s
