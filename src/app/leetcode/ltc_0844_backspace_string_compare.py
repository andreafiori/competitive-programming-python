"""
Backspace string compare | https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

Example 2:
    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

Example 3:
    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

Example 4:
    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

Note:
    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.
    Follow up:

Can you solve it in O(N) time and O(1) space?
"""
class BackspaceStringCompare:

    def compare(self, S: str, T: str) -> bool:
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if S == T:
            return True
        s_stack = []
        t_stack = []
        for c in S:
            if c != '#':
                s_stack.append(c)
            elif len(s_stack) != 0:
                s_stack.pop(-1)
        for c in T:
            if c != '#':
                t_stack.append(c)
            elif len(t_stack) != 0:
                t_stack.pop(-1)
        return ''.join(s_stack) == ''.join(t_stack)
