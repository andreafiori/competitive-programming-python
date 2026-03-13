"""
Degree of an Array | https://leetcode.com/problems/degree-of-an-array/
"""
class DegreeOfAnArray:
    """ #. Degree of an Array """

    def find_shortest_sub_array(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
