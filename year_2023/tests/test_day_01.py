from year_2023.src._utils import get_example_file_path
from year_2023.src.day_01.solution import solve_day_01_part_1, solve_day_01_part_2


def test_example():
    with open(get_example_file_path(1, 1)) as f:
        lines = f.readlines()
    assert solve_day_01_part_1(lines) == 142


def test_example_part_2():
    with open(get_example_file_path(1, 2)) as f:
        lines = f.readlines()
    assert solve_day_01_part_2(lines) == 281
