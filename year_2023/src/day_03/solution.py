import numpy as np

from year_2023.src._utils import get_input_file_path


def solve_part_1(lines: list[str]) -> int:
    schema = np.array([[*line.strip()] for line in lines])
    print(schema.shape)
    for i in schema.shape[0]:
        for j in schema.shape[1]:
            print(i, j)
            pass
            # check_adjacent_symbol(i, j, schema)

    return 10


def solve_part_2(lines: list[str]) -> int:
    return 10


if __name__ == "__main__":
    with open(get_input_file_path(3)) as f:
        lines = f.readlines()
    print(f"Part 1: {solve_part_1(lines)}")
    print(f"Part 2: {solve_part_2(lines)}")
