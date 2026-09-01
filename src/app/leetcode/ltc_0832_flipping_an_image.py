"""
Flipping an Image | leetcode 832 | https://leetcode.com/problems/flipping-an-image/

"""

class FlippingAnImage:
    def flip(self, a):
        for row in a:
            for i in range((len(row) + 1) // 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return a
