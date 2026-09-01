from app.codility.prefix_sums.genomic_range_query import GenomicRangeQuery

class TestGenomicRangeQuery:
    def test_slow_solution(self):
        grq = GenomicRangeQuery()
        S = "CAGCCTA"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        assert grq.slow_solution(S, P, Q) == [2, 4, 1]

    def test_fast_solution(self):
        grq = GenomicRangeQuery()
        S = "CAGCCTA"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        assert grq.fast_solution(S, P, Q) == [2, 4, 1]