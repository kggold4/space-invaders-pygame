from datetime import datetime

from kg_logger import KGLogger


class Timer:
    def __init__(self):
        self.logger = KGLogger()
        self._start_time = datetime.now()
        self._seconds_timer = 0

    def time_pass_in_seconds(self) -> float:
        return (datetime.now() - self._start_time).total_seconds()

    def print_seconds(self):
        if self.time_pass_in_seconds() > self._seconds_timer:
            self.logger.info(f"Time: {self._seconds_timer}")
            self._seconds_timer += 1
