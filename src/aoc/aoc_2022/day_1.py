from typing import Iterable
from itertools import groupby
import heapq


def total_elf_calories(elf_snacks: Iterable[str]) -> int:
    return sum(map(lambda x: int(x) if x != "" else 0, elf_snacks))


def most_calories(input_fp: str) -> int:
    curr_max = 0
    with open(input_fp) as file:
        for k, es in groupby((line.strip("\n") for line in file), lambda x: x != ""):
            if k:
                curr_max = max(curr_max, total_elf_calories(es))

    return curr_max


def top_three_calories(input_fp: str) -> int:
    top_cals: list[int] = []
    with open(input_fp) as file:
        grps = groupby((line.strip("\n") for line in file), lambda x: x != "")
        for k, es in grps:
            if k:
                heapq.heappush(top_cals, total_elf_calories(es))

    return sum(heapq.nlargest(3, top_cals))
