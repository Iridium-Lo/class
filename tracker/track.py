import calendar as c
from datetime import time as t
from decimal import Decimal
from dataclasses import dataclass
from typing import Dict, Iterable, Collection

UNIT = 'u'
SUBSTANCE = 's'


@dataclass
class DailyAverageDose:
    day: int
    time_dose: Dict[float, Decimal]

    @property
    def times(self) -> list[float]:
        return list(self.time_dose.keys())

    @property
    def doses(self) -> list[Decimal]:
        return list(self.time_dose.values())

    @property
    def daily_dose(self) -> Decimal:
        return sum(i for i in self.doses)

    def diff(self, times_doses) -> Iterable:
        return (abs(i - i+1) for i in times_doses)

    def mean(self, times_doses) -> Decimal:
        return sum(i for i in self.diff(times_doses)) / len(times_doses)

    def __str__(self):
        return (
            f'{self.day}: {self.daily_dose}'
            f'Mtime: {self.mean(self.times)}'
            f'Mdose: {self.mean(self.doses)}'
        )


@dataclass
class DoseWeekday:
    day_time_dose: Collection[DailyAverageDose]

    def dose_total(self) -> float:
        return sum(i for i in self.doses.values())

    def weekday_name(self) -> str:
        return (i for i in self.days)

    def __str__(self):
        return f'{self.weekday_name}: {self.dose_total} {UNIT}'


def main():
   days = DoseWeekday(
       day_time_dose=(
           DailyAverageDose(
               day=c.MONDAY,
               time_dose={
                 t(12): 1,
                 t(13): 1,
               },
           ),
           DailyAverageDose(
               day=c.TUESDAY,
               time_dose={
                 t(12): 2,
                 t(14): 2,
               }
           )
       )
   )
   days.echo
