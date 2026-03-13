"""
Maximum Width Ramp | https://leetcode.com/problems/maximum-width-ramp/
"""
class MaximumWidthRamp:

    def max_width_ramp(self, A):
        ans = 0
        m = float('inf')
        # Sort index based on value
        for i in sorted(range(len(A)), key=A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans
