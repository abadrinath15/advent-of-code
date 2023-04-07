from collections import deque
import re


def row_to_instruction(row: str, stacks: list[deque[str]]) -> None:
    matches = re.match(r"move (\d+) from (\d+) to (\d+)", row)
    if matches is None:
        raise ValueError

    how_many, from_s, to_s = (int(matches[x]) for x in range(1, 4))
    from_s -= 1
    to_s -= 1
    while how_many > 0:
        stacks[to_s].append(stacks[from_s].pop())
        how_many -= 1


def row_to_cols(row: str) -> list[int]:
    return [int(num) for num in row.split()]


def row_to_stack(row: str) -> list[str | None]:
    res = []
    while True:
        if len(row) == 0:
            return res

        first_take = row[:3]
        row = row[3:]
        if first_take[0] == "[":
            res.append(first_take[1])
            if len(row) == 0:
                return res

        else:
            res.append(None)

        row = row[1:]


def main(input_fp: str) -> str:
    temp_stacks: list[list[str | None]] = []
    with open(input_fp) as file:
        file_iter = iter(file)
        for line in file_iter:
            if line[1] == "1":
                break

            temp_stacks.append(row_to_stack(line))

        num_stacks = len(row_to_cols(line))
        stacks: list[deque[str]] = [deque() for _ in range(num_stacks)]
        for row in temp_stacks:
            for col, stack in zip(row, stacks):
                if col is not None:
                    stack.appendleft(col)

        next(file_iter)

        for line in file_iter:
            row_to_instruction(line, stacks)

        return "".join(x.pop() for x in stacks)


if __name__ == "__main__":
    print(main("src/aoc/aoc_2022/inputs/day_5.txt"))
