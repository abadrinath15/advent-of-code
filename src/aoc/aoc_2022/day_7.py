import re
from typing import TypeVar, Optional
from dataclasses import dataclass, field
import heapq


@dataclass
class RootDirectory:
    name: str
    parent: None = None
    files: dict[str, "File"] = field(default_factory=dict)
    folders: dict[str, "ChildDirectory"] = field(default_factory=dict)

    size: int = 0


@dataclass
class ChildDirectory:
    name: str
    parent: "Directory"
    files: dict[str, "File"] = field(default_factory=dict)
    folders: dict[str, "ChildDirectory"] = field(default_factory=dict)
    size: int = 0


Directory = RootDirectory | ChildDirectory


@dataclass
class File:
    size: int
    name: str
    parent: RootDirectory | ChildDirectory


T = TypeVar("T", Directory, File)


def contains_folder(dir: Directory, name: str) -> Optional[ChildDirectory]:
    return dir.folders.get(name)


def contains_file(dir: Directory, name: str) -> Optional[File]:
    return dir.files.get(name)


def add_directory_size(
    dir: Directory, sizes: list[int], include_boundary: int = 100000
) -> None:
    size = sum(file.size for file in dir.files.values())
    for folder in dir.folders.values():
        add_directory_size(folder, sizes)
        size += folder.size

    dir.size = size
    sizes.append(size)


def parse_line(line: str, cd: Directory) -> Directory:
    if (re.match(r"\$ cd \.\.", line)) is not None:
        match cd:
            case RootDirectory():
                raise ValueError()

            case ChildDirectory():
                return cd.parent

    if (cd_down := re.match(r"\$ cd (\/|([a-z])+)$", line)) is not None:
        fldr_name = cd_down[1]
        if (child := contains_folder(cd, fldr_name)) is not None:
            return child

        cd.folders["fldr_name"] = (child := ChildDirectory(fldr_name, cd))
        return child

    if (child_file := re.match(r"([0-9]*) ([a-z.]+)", line)) is not None:
        file_size, file_name = int(child_file[1]), child_file[2]
        cd.files[file_name] = File(file_size, file_name, cd)
        return cd

    if (child_dir := re.match(r"dir ([a-z]+)", line)) is not None:
        fldr_name = child_dir[1]
        cd.folders[fldr_name] = ChildDirectory(fldr_name, cd)
        return cd

    return cd


def min_to_remove(
    sizes: list[int], base: Directory, total: int = 70000000, min_space: int = 30000000
) -> int:
    heapq.heapify(sizes)
    existing = total - base.size
    target = min_space - existing
    while True:
        next_pop = heapq.heappop(sizes)
        if next_pop >= target:
            return next_pop


def main(input_fp: str) -> tuple[int, int]:
    cd = base = RootDirectory("\\")
    with open(input_fp) as file:
        file_iter = iter(file)
        next(file_iter)
        for line in file:
            cd = parse_line(line.strip(), cd)

    sizes: list[int] = []
    add_directory_size(base, sizes)
    return sum(filter(lambda x: x < 100000, sizes)), min_to_remove(sizes, base)


if __name__ == "__main__":
    total, remove = main("src/aoc/aoc_2022/inputs/day_7.txt")
    print(total)
    print(remove)
