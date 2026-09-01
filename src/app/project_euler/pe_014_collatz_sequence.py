"""
Problem 14: https://projecteuler.net/problem=14

Collatz conjecture: start with any positive integer n. Next term obtained from
the previous term as follows:

If the previous term is even, the next term is one half the previous term.
If the previous term is odd, the next term is 3 times the previous term plus 1.
The conjecture states the sequence will always reach 1 regardless of starting
n.

Problem Statement:
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

from __future__ import annotations

class CollatzSequence:
    COLLATZ_SEQUENCE_LENGTHS = {1: 1}

    def solution_one(self, n: int = 1000000) -> int:
        """Returns the number under n that generates the longest sequence using the
        formula:
        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

        >>> CollatzSequence().solution_one(1000000)
        837799
        >>> CollatzSequence().solution_one(200)
        171
        >>> CollatzSequence().solution_one(5000)
        3711
        >>> CollatzSequence().solution_one(15000)
        13255
        """
        largest_number = 1
        pre_counter = 1
        counters = {1: 1}

        for input1 in range(2, n):
            counter = 0
            number = input1

            while True:
                if number in counters:
                    counter += counters[number]
                    break
                if number % 2 == 0:
                    number //= 2
                    counter += 1
                else:
                    number = (3 * number) + 1
                    counter += 1

            if input1 not in counters:
                counters[input1] = counter

            if counter > pre_counter:
                largest_number = input1
                pre_counter = counter
        return largest_number

    def collatz_sequence_length(self, n: int) -> int:
        """Returns the Collatz sequence length for n."""
        if n in self.COLLATZ_SEQUENCE_LENGTHS:
            return self.COLLATZ_SEQUENCE_LENGTHS[n]
        next_n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence_length = self.collatz_sequence_length(next_n) + 1
        self.COLLATZ_SEQUENCE_LENGTHS[n] = sequence_length
        return sequence_length


    def solution(self, n: int = 1000000) -> int:
        """Returns the number under n that generates the longest Collatz sequence.

        >>> CollatzSequence().solution(1000000)
        837799
        >>> CollatzSequence().solution(200)
        171
        >>> CollatzSequence().solution(5000)
        3711
        >>> CollatzSequence().solution(15000)
        13255
        """

        result = max((self.collatz_sequence_length(i), i) for i in range(1, n))
        return result[1]
