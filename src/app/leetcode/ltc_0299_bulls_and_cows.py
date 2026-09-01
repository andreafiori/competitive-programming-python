"""
Bulls and Cows | Leetcode 299 | Medium | https://leetcode.com/problems/bulls-and-cows/

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"

Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

Constraints:
1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.
"""

def get_hint(self, secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    check = {}
    ls = len(secret)
    bull, cow = 0, 0
    different = []
    for i in range(ls):
        if guess[i] == secret[i]:
            bull += 1
        else:
            # store possible index and count for cow
            different.append(i)
            try:
                check[secret[i]] += 1
            except KeyError:
                check[secret[i]] = 1
    for i in different:
        try:
            if check[guess[i]] > 0:
                cow += 1
                check[guess[i]] -= 1
        except:
            pass
    return "%dA%dB" % (bull, cow)


"""
s = Solution()
print s.getHint("1122", "1222")
"""
