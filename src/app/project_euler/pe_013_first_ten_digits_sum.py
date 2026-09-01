"""
Problem 13: https://projecteuler.net/problem=13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

import os

class FIrstTenDigitsOfSum:

    def solution(self) -> str:
        """
        Returns the first ten digits of the sum of the array elements
        from the file num.txt

        >>> FIrstTenDigitsOfSum().solution()
        '5537376230'
        """
        file_path = os.path.join(os.path.dirname(__file__), "num.txt")
        with open(file_path) as file_hand:
            return str(sum(int(line) for line in file_hand))[:10]
