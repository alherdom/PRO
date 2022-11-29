# *****************
# FICHO CUANDO TOCA
# *****************


def run(time: str, offset: int) -> str:
    start_time_in_mins = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
    final_time_in_mins = start_time_in_mins + offset
    hours = final_time_in_mins // 60
    mins = final_time_in_mins % 60

    if hours > 24:
        hours = hours - 24

    final_time = f"{hours}:{mins}"
    return final_time


if __name__ == '__main__':
    run('17:15', 240)
