from app.leetcode.ltc_0011_container_with_most_water import ContainerWithMostWater

class TestContainerWithMostWater:
    def test_max_area(self):
        c = ContainerWithMostWater()
        assert c.max_area([1,8,6,2,5,4,8,3,7]) == 49
        assert c.max_area([1,1]) == 1
        assert c.max_area([4,3,2,1,4]) == 16
        assert c.max_area([1,2,1]) == 2