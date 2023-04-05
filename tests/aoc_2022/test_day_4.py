from aoc.aoc_2022 import day_4


def test_camp_cleanup() -> None:
    assert day_4.camp_cleanup("src/aoc/aoc_2022/inputs/day_4_test.txt") == 2


def test_camp_cleanup_2() -> None:
    assert day_4.camp_cleanup_2("src/aoc/aoc_2022/inputs/day_4_test.txt") == 4
