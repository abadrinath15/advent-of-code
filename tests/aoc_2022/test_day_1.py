from aoc.aoc_2022 import day_1


def test_most_calories() -> None:
    assert day_1.most_calories("src/aoc/aoc_2022/inputs/day_1_test.txt") == 24000


def test_top_three_calories() -> None:
    assert day_1.top_three_calories("src/aoc/aoc_2022/inputs/day_1_test.txt") == 45000
