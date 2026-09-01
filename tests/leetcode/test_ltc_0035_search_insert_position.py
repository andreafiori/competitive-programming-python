
from app.leetcode.ltc_0035_search_insert_position import SearchInsertPosition

class TestSearchInsertPosition:
    def test_solution_one(self):
        search_insert_position = SearchInsertPosition()
        assert search_insert_position.solution_one([1, 3, 5, 6], 5) == 2
        assert search_insert_position.solution_one([1, 3, 5, 6], 2) == 1
        assert search_insert_position.solution_one([1, 3, 5, 6], 7) == 4
        assert search_insert_position.solution_one([1, 3, 5, 6], 0) == 0
        assert search_insert_position.solution_one([1], 0) == 0
        assert search_insert_position.solution_one([1], 1) == 0
        assert search_insert_position.solution_one([1], 2) == 1

    def test_solution_two(self):
        search_insert_position = SearchInsertPosition()
        assert search_insert_position.solution_two([1, 3, 5, 6], 5) == 2
        assert search_insert_position.solution_two([1, 3, 5, 6], 2) == 1
        assert search_insert_position.solution_two([1, 3, 5, 6], 7) == 4
        assert search_insert_position.solution_two([1, 3, 5, 6], 0) == 0
        assert search_insert_position.solution_two([1], 0) == 0
        assert search_insert_position.solution_two([1], 1) == 0
        assert search_insert_position.solution_two([1], 2) == 1