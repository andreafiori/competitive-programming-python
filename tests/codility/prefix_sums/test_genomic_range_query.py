import random

from app.codility.prefix_sums.genomic_range_query import GenomicRangeQuery


def test_slow_and_fast_solution_agree_on_example():
    seq = "CAGCCTA"
    p = [2, 5, 0]
    q = [4, 5, 6]
    expected = [2, 4, 1]

    problem = GenomicRangeQuery()

    assert problem.slow_solution(seq, p, q) == expected
    assert problem.fast_solution(seq, p, q) == expected


def test_single_nucleotide_query():
    problem = GenomicRangeQuery()

    assert problem.fast_solution("A", [0], [0]) == [1]
    assert problem.slow_solution("A", [0], [0]) == [1]


def test_all_same_nucleotide_returns_same_impact():
    problem = GenomicRangeQuery()

    assert problem.fast_solution("CCCC", [0, 1, 2], [0, 2, 3]) == [2, 2, 2]
    assert problem.slow_solution("CCCC", [0, 1, 2], [0, 2, 3]) == [2, 2, 2]


def test_fast_solution_matches_slow_solution_for_random_queries():
    random.seed(42)
    problem = GenomicRangeQuery()
    letters = "ACGT"
    seq = "".join(random.choice(letters) for _ in range(100))

    p = [random.randrange(0, len(seq)) for _ in range(20)]
    q = [random.randrange(start, len(seq)) for start in p]

    assert problem.fast_solution(seq, p, q) == problem.slow_solution(seq, p, q)
