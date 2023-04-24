from aoc.aoc_2022 import day_7


def test_main() -> None:
    total, remove = day_7.main("src/aoc/aoc_2022/inputs/day_7_test.txt")
    assert total == 95437
    assert remove == 24933642
