from aoc.aoc_2022 import day_5


def test_row_to_cols() -> None:
    test_res = day_5.row_to_cols(" 1   2   3 ")
    assert test_res == [1, 2, 3]


def test_row_to_stack() -> None:
    assert day_5.row_to_stack("    [D]    \n") == [None, "D", None]
    assert day_5.row_to_stack("[N] [C]    \n") == ["N", "C", None]
