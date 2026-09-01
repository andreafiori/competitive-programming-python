"""
Leetcode Problem: 68. Text Justification | https://leetcode.com/problems/text-justification/
"""

class TextJustification:

    def solution(self, words: list[str], max_width: int) -> list[str]:
        """
        :param words: list of words to be justified
        :param max_width: the maximum width of each line
        :return: list of justified text lines
        """
        i, N, result = 0, len(words), []
        while i < N:
            one_line, j, curr_width, position_num, space_num = [words[i]], i + 1, len(words[i]), 0, max_width - len(words[i])
            while j < N and curr_width + 1 + len(words[j]) <= max_width:
                one_line.append(words[j])
                curr_width += 1 + len(words[j])
                space_num -= len(words[j])
                position_num, j = position_num + 1, j + 1
            i = j
            # decide the layout of one line
            if i < N and position_num:
                spaces = [' ' * (space_num // position_num + (k < space_num % position_num)) for k in range(position_num)] + [
                    '']
            else:  # last line or the line only has one word
                spaces = [' '] * position_num + [' ' * (max_width - curr_width)]
            result.append(''.join([s for pair in zip(one_line, spaces) for s in pair]))
        return result
