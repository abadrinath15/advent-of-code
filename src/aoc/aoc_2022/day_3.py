import os
from functools import reduce
from itertools import islice


def prioritize_item(item: str) -> int:
    if (item_ord := ord(item)) > 96:
        return item_ord - 96

    return item_ord - 38


def rucksack_reorganization(input_fp: os.PathLike[str]) -> int:
    score = 0
    with open(input_fp) as file:
        for line in file:
            line = line.strip("\n")
            first, second = line[: (half_line := int(len(line) / 2))], line[half_line:]
            score += prioritize_item(set(first).intersection(second).pop())

    return score


def rucksack_reorganization_2(input_fp: os.PathLike[str]) -> int:
    with open(input_fp) as file:
        file_iter = iter(file)
        score = 0
        while True:
            elf_group = islice(file_iter, 3)
            elf_sets = map(lambda a: set(a.strip("\n")), elf_group)
            try:
                most_common = reduce(lambda a, b: a.intersection(b), elf_sets)
            except TypeError:
                return score

            score += prioritize_item(most_common.pop())
