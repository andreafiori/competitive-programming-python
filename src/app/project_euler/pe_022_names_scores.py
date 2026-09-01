"""
Problem 22 | https://projecteuler.net/problem=22

Name scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

import os

class NamesScorres:

    def solution_one(self):
        """Returns the total of all the name scores in the file.

        >>> NamesScorres().solution_one()
        871198282
        """
        with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
            names = str(file.readlines()[0])
            names = names.replace('"', "").split(",")

        names.sort()

        name_score = 0
        total_score = 0

        for i, name in enumerate(names):
            for letter in name:
                name_score += ord(letter) - 64

            total_score += (i + 1) * name_score
            name_score = 0
        return total_score

    def solution_two(self):
        """Returns the total of all the name scores in the file.

        >>> NamesScorres().solution_two()
        871198282
        """
        total_sum = 0
        temp_sum = 0
        with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
            name = str(file.readlines()[0])
            name = name.replace('"', "").split(",")

        name.sort()
        for i in range(len(name)):
            for j in name[i]:
                temp_sum += ord(j) - ord("A") + 1
            total_sum += (i + 1) * temp_sum
            temp_sum = 0
        return total_sum
