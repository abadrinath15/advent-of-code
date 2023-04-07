from aoc.aoc_2022 import day_5
from collections import deque


def test_row_to_instruction() -> None:
    stacks = [deque(["Z", "N"]), deque(["M", "C", "D"]), deque(["P"])]
    day_5.row_to_instruction("move 1 from 2 to 1", stacks)
    assert stacks == [deque(["Z", "N", "D"]), deque(["M", "C"]), deque(["P"])]


def test_row_to_cols() -> None:
    test_res = day_5.row_to_cols(" 1   2   3 ")
    assert test_res == [1, 2, 3]


def test_row_to_stack() -> None:
    assert day_5.row_to_stack("    [D]    \n") == [None, "D", None]
    assert day_5.row_to_stack("[N] [C]    \n") == ["N", "C", None]


def test_main() -> None:
    assert day_5.main("src/aoc/aoc_2022/inputs/day_5_test.txt") == "CMZ"
    assert day_5.main("src/aoc/aoc_2022/inputs/day_5_test.txt", pop_bunch=True) == "MCD"
