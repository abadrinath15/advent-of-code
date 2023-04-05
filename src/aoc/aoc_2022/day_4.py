from pathlib import Path


def camp_cleanup(input_fp: Path[str]) -> int:
    overlapping_counts = 0
    with open(input_fp) as file:
        for line in file:
            first, second = line.split(",")
            max_1, min_1 = [int(x) for x in first.split("-")]
            max_2, min_2 = [int(x) for x in second.split("-")]
            if (min_1 >= min_2 and max_1 <= max_2) or (
                min_2 >= min_1 and max_2 <= max_1
            ):
                overlapping_counts += 1

    return overlapping_counts


def camp_cleanup_2(input_fp: Path[str]) -> int:
    overlapping_counts = 0
    with open(input_fp) as file:
        for line in file:
            first, second = line.split(",")
            min_1, max_1 = [int(x) for x in first.split("-")]
            min_2, max_2 = [int(x) for x in second.split("-")]
            if (min_2 <= min_1 <= max_2) or (min_1 <= min_2 <= max_1):
                overlapping_counts += 1

    return overlapping_counts


def main() -> None:
    print(camp_cleanup("src/aoc/aoc_2022/inputs/day_4.txt"))
    print(camp_cleanup_2("src/aoc/aoc_2022/inputs/day_4.txt"))


if __name__ == "__main__":
    main()
