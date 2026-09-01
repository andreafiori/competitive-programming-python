"""
Problem 25: 1000-digit Fibonacci number | https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""
from collections.abc import Generator

class Fibonacci:

    def solution_one(self, n: int) -> int:
        """
        Computes the Fibonacci number for input n by iterating through n numbers
        and creating an array of ints using the Fibonacci formula.
        Returns the nth element of the array.

        >>> Fibonacci().solution_one(2)
        1
        >>> Fibonacci().solution_one(3)
        2
        >>> solution_one(5)
        5
        >>> Fibonacci().solution_one(10)
        55
        >>> Fibonacci().solution_one(12)
        144

        """
        if n == 1 or not isinstance(n, int):
            return 0
        elif n == 2:
            return 1
        else:
            sequence = [0, 1]
            for i in range(2, n + 1):
                sequence.append(sequence[i - 1] + sequence[i - 2])

            return sequence[n]


    def _digits_index(self, n: int) -> int:
        """
        Computes incrementing Fibonacci numbers starting from 3 until the length
        of the resulting Fibonacci result is the input value n. Returns the term
        of the Fibonacci sequence where this occurs.

        >>> Fibonacci()._digits_index(1000)
        4782
        >>> Fibonacci()._digits_index(100)
        476
        >>> Fibonacci()._digits_index(50)
        237
        >>> Fibonacci()._digits_index(3)
        12
        """
        digits = 0
        index = 2

        while digits < n:
            index += 1
            digits = len(str(self.solution_one(index)))

        return index

    def solution_digits_index(self, n: int = 1000) -> int:
        """
        Returns the index of the first term in the Fibonacci sequence to contain
        n digits.

        >>> Fibonacci().solution(1000)
        4782
        >>> Fibonacci().solution(100)
        476
        >>> Fibonacci().solution(50)
        237
        >>> Fibonacci().solution(3)
        12
        """
        return self._digits_index(n)

    def _generator(self) -> Generator[int]:
        """
        A generator that produces numbers in the Fibonacci sequence

        >>> generator = Fibonacci()._generator()
        >>> next(generator)
        1
        >>> next(generator)
        2
        >>> next(generator)
        3
        >>> next(generator)
        5
        >>> next(generator)
        8
        """
        a, b = 0, 1
        while True:
            a, b = b, a + b
            yield b


    def solution_generator(self, n: int = 1000) -> int:
        """Returns the index of the first term in the Fibonacci sequence to contain
        n digits.

        >>> Fibonacci().solution_generator(1000)
        4782
        >>> Fibonacci().solution_generator(100)
        476
        >>> Fibonacci().solution_generator(50)
        237
        >>> Fibonacci().solution_generator(3)
        12
        """
        answer = 1
        gen = self._generator()
        while len(str(next(gen))) < n:
            answer += 1
        return answer + 1


    def solution_three(self, n: int = 1000) -> int:
        """Returns the index of the first term in the Fibonacci sequence to contain
        n digits.

        >>> Fibonacci().solution_three(1000)
        4782
        >>> Fibonacci().solution_three(100)
        476
        >>> Fibonacci().solution_three(50)
        237
        >>> Fibonacci().solution_three(3)
        12
        """
        f1, f2 = 1, 1
        index = 2
        while True:
            i = 0
            f = f1 + f2
            f1, f2 = f2, f
            index += 1
            for _ in str(f):
                i += 1
            if i == n:
                break
        return index
