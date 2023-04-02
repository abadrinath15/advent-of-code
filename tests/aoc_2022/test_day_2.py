from aoc.aoc_2022 import day_2


def test_rock_paper_scissors() -> None:
    assert day_2.rock_paper_scissors("src/aoc/aoc_2022/inputs/day_2_test.txt") == 15


def test_rock_paper_scissors_2() -> None:
    assert day_2.rock_paper_scissors_2("src/aoc/aoc_2022/inputs/day_2_test.txt") == 12
