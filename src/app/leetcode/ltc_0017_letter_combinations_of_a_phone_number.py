"""
Letter Combinations of a Phone Number | LeetCode 17 | https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""

class LetterCombinations:
    dmap = {'2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' ',
        None: None
    }

    def solution(self, digits: str) -> list[str]:
        # DFS
        result = []
        ls = len(digits)
        if ls == 0:
            return result
        current = digits[0]
        posfix = self.solution(digits[1:])
        for t in self.dmap[current]:
            if len(posfix) > 0:
                for p in posfix:
                    temp = t + p
                    result.append(temp)
            else:
                result.append(t)
        return result
