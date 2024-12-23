def get_input_file_path(day: int) -> str:
    if day < 10:
        return f"year_2024/data/input_0{day}.txt"
    return f"year_2024/data/input_{day}.txt"


def get_example_file_path(day: int, part: int) -> str:
    if day < 10:
        return f"data/example_0{day}_part_{part}.txt"
    return f"year_2024/data/example_{day}_part_{part}.txt"
