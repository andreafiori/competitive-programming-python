"""
Power of Three | https://leetcode.com/problems/power-of-three/
"""
class PowerOfThree:

    def is_power_of_three(self, n: int) -> bool:
        max3pow = 1162261467
        if n <= 0 or n > max3pow:
            return False
        return max3pow % n == 0
