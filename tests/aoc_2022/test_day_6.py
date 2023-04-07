from aoc.aoc_2022 import day_6


def test_main() -> None:
    assert day_6.main("src/aoc/aoc_2022/inputs/day_6_test.txt") == 7
    assert day_6.main("src/aoc/aoc_2022/inputs/day_6_test.txt", max_dq_size=13) == 19
