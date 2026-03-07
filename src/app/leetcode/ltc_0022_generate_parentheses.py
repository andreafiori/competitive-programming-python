"""
Generate Parentheses | https://leetcode.com/problems/generate-parentheses/

"""

class GenerateParentheses:

    def generate(self, n: int) -> list[str]:
        if n == 1:
            return ['()']
        last_list = self.generate(n - 1)
        res = []
        for t in last_list:
            curr = t + ')'
            for index in range(len(curr)):
                if curr[index] == ')':
                    res.append(curr[:index] + '(' + curr[index:])
        return list(set(res))

