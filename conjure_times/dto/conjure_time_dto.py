from dataclasses import dataclass
from datetime import datetime


@dataclass
class LogConjureTimeDto:
    epoch: int
    seconds: int
    start_cut: datetime
    end_cut: datetime
