from year_2023.src._utils import get_example_file_path
from year_2023.src.day_02.solution import solve_part_1, solve_part_2


def test_example():
    with open(get_example_file_path(2, 1)) as f:
        lines = f.readlines()
    assert solve_part_1(lines) == 8


def test_example_part_2():
    with open(get_example_file_path(2, 2)) as f:
        lines = f.readlines()
    assert solve_part_2(lines) == 2286
