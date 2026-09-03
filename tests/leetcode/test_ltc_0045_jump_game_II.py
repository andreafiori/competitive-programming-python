from app.leetcode.ltc_0045_jump_game_II import JumpGameII

class TestJumpGameII:
    def test_jump(self):
        jg = JumpGameII()
        assert jg.solution([2, 3, 1, 1, 4]) == 2
        assert jg.solution([2, 3, 0, 1, 4]) == 2
        assert jg.solution([1, 2]) == 1
        assert jg.solution([1, 2, 3]) == 2
        assert jg.solution([1, 1, 1]) == 2
        assert jg.solution([1, 1, 1, 1]) == 3
        assert jg.solution([0]) == 0
        assert jg.solution([1]) == 0
        assert jg.solution([2, 0]) == 1