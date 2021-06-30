import calendar as c
from datetime import time as t
from decimal import Decimal
from dataclasses import dataclass
from typing import Dict, Iterable, Collection, List

UNIT = 'u'
SUBSTANCE = 's'


@dataclass
class DailyDoseMean:
    day: int
    time_dose: Dict[float, Decimal]

    @property
    def times(self) -> List[float]:
        return round(
            list(
                self.time_dose
                .keys()
            ), 4
        )

    @property
    def doses(self) -> List[Decimal]:
        return round(
            list(
                self.time_dose
                .values()
            ), 2
        )
        

    @property
    def daily_dose(self) -> Decimal:
        return sum(i for i in self.doses)

    def diff(self) -> Iterable:
        return (
            abs(
                self.lst[i] - self.lst[i+1]
            ) for i in enumerate(self.lst - 1)
        )

    def mean(self) -> Decimal:
        return sum(
            i for i in self.diff(self.lst)
            ) / len(self.lst)

    def __str__(self):
        return (
            f'{self.day}: {self.daily_dose}'
            f'Mtime: {self.mean(self.times)}'
            f'Mdose: {self.mean(self.doses)}'
        )


@dataclass
class WeeklyDose:
    day_dose_mean: Collection[DailyAverageDose]

    @property
    def weekly_dose(self) -> float:
        return sum(i.daily_dose for i in self.day_dose_mean)

    @property
    def echo(self):
        print('\n'.join(i.str for i in self.day_dose_mean))
        print(f'Weekly dose -> {SUBSTANCE}: {self.weekly_dose} {UNIT}'


def main():
   days = WeeklyDose(
       day_dose_mean=(
           DailyDoseMean(
               day=c.MONDAY,
               time_dose={
                 t(12): 1,
                 t(13): 1,
               },
           ),
           DailyDoseMean(
               day=c.TUESDAY,
               time_dose={
                 t(12): 2,
                 t(14): 2
               }
           )
       )
   )
   days.echo

if __name__ == '__main__':
    main()
