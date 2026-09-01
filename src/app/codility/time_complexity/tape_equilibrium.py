"""
Tape Equilibrium | http://codility.com/demo/take-sample-test/tape_equilibrium

The variable of head stores the sum of the heading part of the tape. And the variable of tail stores the sum of tailing part.

Then, we move the index from 2nd position to the last 2nd position.

Every time we move the index, we adjust both head and tail, compute and compare the difference.

"""

class TapeEquilibrium:
    def solution(self, a):
        """
        Minimize the value |(a[0] + ... + a[P-1]) - (a[P] + ... + a[N-1])|.
        :param a: non-empty list of integers
        :return: minimal difference between two partitions
        """
        if len(a) < 2:
            raise ValueError("Array must contain at least two elements")

        before = a[0]
        after = sum(a) - a[0]
        best = abs(before - after)

        for P in range(1, len(a) - 1):
            before += a[P]
            after -= a[P]
            best = min(best, abs(before - after))

        return best
