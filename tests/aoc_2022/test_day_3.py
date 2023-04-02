from aoc.aoc_2022 import day_3


def test_rucksack_reorganization() -> None:
    assert (
        day_3.rucksack_reorganization("src/aoc/aoc_2022/inputs/day_3_test.txt") == 157
    )


def test_rucksack_reorganization_2() -> None:
    assert (
        day_3.rucksack_reorganization_2("src/aoc/aoc_2022/inputs/day_3_test.txt") == 70
    )
