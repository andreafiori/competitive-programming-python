"""
Leetcode Problem 20: Valid Parentheses | https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

class ValidParentheses:

    def solution(self, s: str) -> bool:
        """
        :param s: str
        :return: bool
        """
        para = {')': '(', ']': '[', '}': '{'}
        op = ['(', '[', '{']
        stack = []

        for c in s:
            if c in op:
                stack.append(c)

            elif c in para:
                if len(stack) != 0 and stack[-1] == para[c]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False