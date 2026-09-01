"""
Coin sums | Problem 31: https://projecteuler.net/problem=31

In England the currency is made up of pound, f, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, f1 (100p) and f2 (200p).
It is possible to make f2 in the following way:

1xf1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can f2 be made using any number of coins?

Hint:
    > There are 100 pence in a pound (f1 = 100p)
    > There are coins(in pence) are available: 1, 2, 5, 10, 20, 50, 100 and 200.
    > how many different ways you can combine these values to create 200 pence.

Example:
    to make 6p there are 5 ways
      1,1,1,1,1,1
      1,1,1,1,2
      1,1,2,2
      2,2,2
      1,5
    to make 5p there are 4 ways
      1,1,1,1,1
      1,1,1,2
      1,2,2
      5
"""

class CoinSums:

    def one_pence(self) -> int:
        return 1

    def two_pence(self, x: int) -> int:
        return 0 if x < 0 else self.two_pence(x - 2) + self.one_pence()

    def five_pence(self, x: int) -> int:
        return 0 if x < 0 else self.five_pence(x - 5) + self.two_pence(x)

    def ten_pence(self, x: int) -> int:
        return 0 if x < 0 else self.ten_pence(x - 10) + self.five_pence(x)

    def twenty_pence(self, x: int) -> int:
        return 0 if x < 0 else self.twenty_pence(x - 20) + self.ten_pence(x)

    def fifty_pence(self, x: int) -> int:
        return 0 if x < 0 else self.fifty_pence(x - 50) + self.twenty_pence(x)

    def one_pound(self, x: int) -> int:
        return 0 if x < 0 else self.one_pound(x - 100) + self.fifty_pence(x)

    def two_pound(self, x: int) -> int:
        return 0 if x < 0 else self.two_pound(x - 200) + self.one_pound(x)

    def solution(self, n: int = 200) -> int:
        """Returns the number of different ways can n pence be made using any number of
        coins?

        >>> CoinSums().solution(500)
        6295434
        >>> CoinSums().solution(200)
        73682
        >>> CoinSums().solution(50)
        451
        >>> CoinSums().solution(10)
        11
        """
        return self.two_pound(n)

    def solution_two(self, pence: int = 200) -> int:
        """Returns the number of different ways to make X pence using any number of coins.
        The solution is based on dynamic programming paradigm in a bottom-up fashion.

        >>> CoinSums().solution_two(500)
        6295434
        >>> CoinSums().solution_two(200)
        73682
        >>> CoinSums().solution_two(50)
        451
        >>> CoinSums().solution_two(10)
        11
        """
        coins = [1, 2, 5, 10, 20, 50, 100, 200]
        number_of_ways = [0] * (pence + 1)
        number_of_ways[0] = 1  # base case: 1 way to make 0 pence

        for coin in coins:
            for i in range(coin, pence + 1, 1):
                number_of_ways[i] += number_of_ways[i - coin]
        return number_of_ways[pence]
