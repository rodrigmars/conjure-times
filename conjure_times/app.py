from datetime import datetime
from core.calculate_time_core import get_seconds


def main(config: dict[str, str]) -> None:

    get_seconds(config)(datetime.now())([2, 3, 5, 6], 5)


if __name__ == "__main__":

    try:

        config: dict = {"path_file_log": "log_conjure_time.txt"}

        main(config)

        # exit(0)

    except Exception as er:
        print("Error:", er)
        exit(1)
