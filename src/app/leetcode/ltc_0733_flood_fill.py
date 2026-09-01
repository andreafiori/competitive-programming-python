"""
Flood Fill | leetcode 733 | https://leetcode.com/problems/flood-fill/

"""

class FloodFill:

    def fill(self, image, sr, sc, new_color):
        r_ls, c_ls = len(image), len(image[0])
        color = image[sr][sc]
        if color == new_color:
            return image
        queue = [(sr, sc)]
        while len(queue) > 0:
            r, c = queue.pop(0)
            if image[r][c] == color:
                image[r][c] = new_color
                if r - 1 >= 0: queue.append((r - 1, c))
                if r + 1 < r_ls: queue.append((r + 1, c))
                if c - 1 >= 0: queue.append((r, c - 1))
                if c + 1 < c_ls: queue.append((r, c + 1))
        return image
