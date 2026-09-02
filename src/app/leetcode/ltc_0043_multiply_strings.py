"""
Multiply Strings | leetcode 43 | https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

"""

class MultiplyStrings:

    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        res = ''
        ls1, ls2, = len(num1), len(num2)
        ls = ls1 + ls2
        # list stores int
        arr = [0] * ls
        for i in reversed(range(ls1)):
            for j in reversed(range(ls2)):
                # store the direct results of multiply two ints
                arr[i + j + 1] += int(num1[i]) * int(num2[j])
        for i in reversed(range(1, ls)):
            # digital plus
            arr[i - 1] += arr[i] / 10
            arr[i] %= 10
        pos = 0
        # to string
        if arr[pos] == 0:
            pos += 1
        while pos < ls:
            res = res + str(arr[pos])
            pos += 1
        return res
