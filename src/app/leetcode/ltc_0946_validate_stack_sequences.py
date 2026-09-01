"""
Leetcode Problem: 946. Validate Stack Sequences | https://leetcode.com/problems/validate-stack-sequences/
"""

class ValidateStackSequences:

    def solution(self, pushed: list[int], popped: list[int]) -> bool:
        """
        # :type pushed: List[int]
        # :type popped: List[int]
        # :rtype: bool
        """
        in_stack = []
        pos = 0
        while pos != len(pushed):
            curr = pushed[pos]
            while len(in_stack) > 0 and len(popped) > 0 and in_stack[-1] == popped[0]:
                in_stack.pop(-1)
                popped.pop(0)
            if len(popped) == 0:
                break
            if curr == popped[0]:
                popped.pop(0)
            else:
                in_stack.append(curr)
            pos += 1
        while len(in_stack) > 0 and len(popped) > 0 and in_stack[-1] == popped[0]:
            in_stack.pop(-1)
            popped.pop(0)
        if len(in_stack) == 0:
            return True
        return False
