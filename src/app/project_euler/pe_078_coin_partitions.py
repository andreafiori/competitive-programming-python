"""
Problem 78: Coin Partitions | https://projecteuler.net/problem=78

Let p(n) represent the number of different ways in which n coins
can be separated into piles. For example, five coins can be separated
into piles in exactly seven different ways, so p(5)=7.

            OOOOO
            OOOO   O
            OOO   OO
            OOO   O   O
            OO   OO   O
            OO   O   O   O
            O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""

import itertools

class CoinPartitions:

    def solution(self, number: int = 1000000) -> int:
        """
        >>> CoinPartitions().solution(1)
        1

        >>> CoinPartitions().solution(9)
        14

        >>> CoinPartitions().solution()
        55374
        """
        partitions = [1]

        for i in itertools.count(len(partitions)):
            item = 0
            for j in itertools.count(1):
                sign = -1 if j % 2 == 0 else +1
                index = (j * j * 3 - j) // 2
                if index > i:
                    break
                item += partitions[i - index] * sign
                item %= number
                index += j
                if index > i:
                    break
                item += partitions[i - index] * sign
                item %= number

            if item == 0:
                return i
            partitions.append(item)

        return 0
