from collections import deque, Counter


def main(input_fp: str, max_dq_size: int = 3) -> int:
    dq: deque[str] = deque()
    counter: Counter[str] = Counter()
    with open(input_fp) as file:
        for _ in range(max_dq_size):
            char = file.read(1)
            dq.append(char)
            counter[char] += 1

        while (char := file.read(1)) != "":
            max_dq_size += 1
            counter[char] += 1
            if counter.most_common(1)[0][1] == 1:
                return max_dq_size

            counter[dq.popleft()] -= 1
            dq.append(char)

        raise ValueError


if __name__ == "__main__":
    print(main("src/aoc/aoc_2022/inputs/day_6.txt"))
    print(main("src/aoc/aoc_2022/inputs/day_6.txt", max_dq_size=13))
