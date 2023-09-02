from datetime import datetime, timedelta
from time import sleep
from random import choice
from collections.abc import Iterator
from collections.abc import Callable
from dto.conjure_time_dto import LogConjureTimeDto


def get_seconds(config: dict[str, str]) -> Callable[[datetime], Callable]:
    """
    Gets the difference in seconds by subtracting two time windows (data and time).
    Calculates the difference between (date time of elapsed time) and (date time given).

    :(path_file: str)

    :(start_datetime: datetime)

    :(list_seconds: list[int], total_epochs: int)

    :return 
        init(start_datetime: datetime) - Initialize variables and need settings
        check_seconds(list_seconds: list[int], total_epochs: int) - Runs the check between dates
    """
    def init(start_datetime: datetime) -> Callable[[list[int], int], None]:

        def get_seconds(end_cut: datetime, start_cut: datetime) -> int:
            return (end_cut - start_cut).seconds

        def finite_time_mock(seconds: list[int], total_epochs: int) -> Iterator[int]:

            for epoch in range(total_epochs):

                sleep(choice(seconds))

                yield epoch

        def log_time(log: LogConjureTimeDto) -> None:

            with open(config["path_file_log"], 'a') as f:
                f.write(f"{'epoch':8}:{log.epoch}\n")
                f.write(f"{'seconds':8}:{log.seconds}\n")
                f.write(f"{'start_cut':8}:{log.start_cut}\n")
                f.write(f"{'end_cut':8}:{log.end_cut}\n")
                f.write("------------------------\n")

        def check_seconds(list_seconds: list[int], total_epochs: int) -> None:

            start_cut: datetime = start_datetime

            current_time: datetime | None = None
            seconds: int = 0

            for epoch in finite_time_mock(list_seconds, total_epochs):

                current_time = datetime.now()

                seconds = get_seconds(current_time, start_cut)

                start_cut = current_time - \
                    timedelta(seconds=seconds)

                log_time(LogConjureTimeDto(
                    epoch, seconds, start_cut, current_time))

                start_cut = current_time

        return check_seconds

    return init
