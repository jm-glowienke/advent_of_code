from year_2023.src._utils import get_input_file_path


def solve_day_01_part_1(lines: list[str]) -> int:
    codes = []
    for line in lines:
        tmp = [el for el in line if el.isnumeric()]
        codes.append(int(tmp[0] + tmp[-1]))

    return sum(codes)


def solve_day_01_part_2(lines: list[str]) -> int:
    mapping = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seve": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }

    lines_modified = []
    for line in lines:
        for key in mapping:
            if key in line:
                line = line.replace(key, str(mapping.get(key)))
        lines_modified.append(line)
    return solve_day_01_part_1(lines_modified)


with open(get_input_file_path(1)) as f:
    lines = f.readlines()
print(f"Part 1: {solve_day_01_part_1(lines)}")
print(f"Part 2: {solve_day_01_part_2(lines)}")
