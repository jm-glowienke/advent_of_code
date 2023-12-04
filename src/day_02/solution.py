import math
from functools import reduce

from src._utils import get_input_file_path

MAX_COUNTS = {"red": 12, "green": 13, "blue": 14}
NUMBER = 1


def solve_part_1(lines: list[str]) -> int:
    games = {}
    for idx, line in enumerate(lines):
        line_game_remove = line.split(":")[1]
        revelations = line_game_remove.split(";")
        for reveal in revelations:
            for el in reveal.split(","):
                count, color = el.strip(" ").split(" ")
                if int(count) > MAX_COUNTS[color.strip("\n")]:
                    games[idx + 1] = False
        if games.get(idx + 1) is not False:
            games[idx + 1] = True

    return sum(k for k, v in games.items() if v)


def solve_part_2(lines: list[str]) -> int:
    powers = []
    for line in lines:
        min_counts = {"red": NUMBER, "green": NUMBER, "blue": NUMBER}

        line_game_remove = line.split(":")[1]
        revelations = line_game_remove.split(";")
        for reveal in revelations:
            for el in reveal.split(","):
                count, color = el.strip(" ").split(" ")
                if int(count) > min_counts[color.strip("\n")]:
                    min_counts[color.strip("\n")] = int(count)

        powers.append(reduce((lambda x, y: x * y), list(min_counts.values())))

    return sum(powers)


if __name__ == "__main__":
    with open(get_input_file_path(2)) as f:
        lines = f.readlines()
    print(f"Part 1: {solve_part_1(lines)}")
    print(f"Part 2: {solve_part_2(lines)}")
