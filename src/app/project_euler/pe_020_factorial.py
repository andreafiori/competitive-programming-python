"""
Problem 20: https://projecteuler.net/problem=20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
from math import factorial

class Factorial:

    def solution(self, num: int = 100) -> int:
        """Returns the sum of the digits in the factorial of num
        >>> Factorial().solution(100)
        648
        >>> Factorial().solution(50)
        216
        >>> Factorial().solution(10)
        27
        >>> Factorial().solution(5)
        3
        >>> Factorial().solution(3)
        6
        >>> Factorial().solution(2)
        2
        >>> Factorial().solution(1)
        1
        """
        nfact = self._calculate(num)
        result = self._split_and_add(nfact)
        return result

    def solution_two(self, num: int = 100) -> int:
        """Returns the sum of the digits in the factorial of num
        >>> Factorial().solution_two(100)
        648
        >>> Factorial().solution_two(50)
        216
        >>> Factorial().solution_two(10)
        27
        >>> Factorial().solution_two(5)
        3
        >>> Factorial().solution_two(3)
        6
        >>> Factorial().solution_two(2)
        2
        >>> Factorial().solution_two(1)
        1
        """
        return sum(int(x) for x in str(factorial(num)))

    def solution_three(self, num: int = 100) -> int:
        """Returns the sum of the digits in the factorial of num
        >>> Factorial().solution_three(1000)
        10539
        >>> Factorial().solution_three(200)
        1404
        >>> Factorial().solution_three(100)
        648
        >>> Factorial().solution_three(50)
        216
        >>> Factorial().solution_three(10)
        27
        >>> Factorial().solution_three(5)
        3
        >>> Factorial().solution_three(3)
        6
        >>> Factorial().solution_three(2)
        2
        >>> Factorial().solution_three(1)
        1
        >>> Factorial().solution_three(0)
        1
        """
        return sum(map(int, str(factorial(num))))


    def solution_four(self, num: int = 100) -> int:
        """Returns the sum of the digits in the factorial of num
        >>> Factorial().solution_four(100)
        648
        >>> Factorial().solution_four(50)
        216
        >>> Factorial().solution_four(10)
        27
        >>> Factorial().solution_four(5)
        3
        >>> Factorial().solution_four(3)
        6
        >>> Factorial().solution_four(2)
        2
        >>> Factorial().solution_four(1)
        1
        """
        fact = 1
        result = 0
        for i in range(1, num + 1):
            fact *= i

        for j in str(fact):
            result += int(j)

        return result

    def _calculate(self, num: int) -> int:
        """Find the factorial of a given number n"""
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact

    def _split_and_add(self, number: int) -> int:
        """Split number digits and add them."""
        sum_of_digits = 0
        while number > 0:
            last_digit = number % 10
            sum_of_digits += last_digit
            number = number // 10  # Removing the last_digit from the given number
        return sum_of_digits
