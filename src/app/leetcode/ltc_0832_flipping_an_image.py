"""
Flipping an Image | https://leetcode.com/problems/flipping-an-image/
"""
class FlippingAnImage:

    def flip(self, a: int) -> int:
        for row in a:
            for i in range((len(row) + 1) / 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return a
