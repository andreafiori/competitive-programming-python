"""
Most Common Word | leetcode 819 | https://leetcode.com/problems/most-common-word/

https://leetcode.com/problems/most-common-word/discuss/193268/python-one-liner
"""

class MostCommonWord:
    def solution(self, paragraph: str, banned: list[str]) -> str:
        """
        :param paragraph: str
        :param banned: list[str]
        :return: str
        """
        banned = set(banned)
        count = collections.Counter(word for word in re.split('[ !?\',;.]',paragraph.lower()) if word)
        return max((item for item in count.items() if item[0] not in banned), key=operator.itemgetter(1))[0]
