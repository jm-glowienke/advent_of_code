from year_2024._utils import get_input_file_path


def solve_day_01_part_1(lines: list[str]) -> int:
    first_list = []
    second_list = []
    for line in lines:
        first_element, second_element = line.rstrip("\n").split()
        first_list.append(int(first_element))
        second_list.append(int(second_element))

    first_list.sort()
    second_list.sort()

    return sum(
        [abs(b_i - a_i) for a_i, b_i in zip(first_list, second_list, strict=False)]
    )


def solve_day_01_part_2(lines: list[str]) -> int:
    first_list = []
    second_list = []
    for line in lines:
        first_element, second_element = line.rstrip("\n").split()
        first_list.append(int(first_element))
        second_list.append(int(second_element))

    similarity_score = 0
    for el in first_list:
        similarity_score += sum(i for i in second_list if i == el)

    return similarity_score


with open(get_input_file_path(1)) as f:
    lines = f.readlines()
print(f"Part 1: {solve_day_01_part_1(lines)}")
print(f"Part 2: {solve_day_01_part_2(lines)}")
