from itertools import groupby


def most_calories(input_fp: str) -> int:
    curr_max = 0
    with open(input_fp) as file:
        for _, g in groupby((line.strip("\n") for line in file), lambda x: x == ""):
            curr_max = max(curr_max, sum(map(lambda x: int(x) if x != "" else 0, g)))

    return curr_max
