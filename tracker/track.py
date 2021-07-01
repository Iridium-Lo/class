import calendar as c
from datetime import time as t
from decimal import Decimal as dec
from dataclasses import dataclass
from typing import List, Dict, Decimal, Iterable, Collection

UNIT = 'u'
SUBSTANCE = 's'


@dataclass
class DailyDoseMean:
    day: int
    time_dose: Dict[float, float]
    
  @property
    def daily_dose(self) -> Decimal:
        return sum(i for i in self.doses)

    def mean_lst(self, key_val, num) -> Decimal:
        return self.mean(self.lst(key_val, num))

    def mean(self, lst) -> Decimal:
        return sum(
            i for i in self.diff(self.lst)
        ) / len(self.lst)

    def diff(self, lst) -> Iterable[Decimal]:
        return (
            abs(
                self.lst[i] - self.lst[i+1]
            ) for i in enumerate(self.lst - 1)
        )

    def lst(self, key_val, num) -> List[Decimal]:
        return dec(
            round(
                list(
                    self.time_dose
                    .key_val()
                ), num
            )
        )

    def __str__(self):
        return (
            f'{self.day}: {self.daily_dose}'
            f'Mtime: {self.mean_lst(keys, 4)}'
            f'Mdose: {self.mean_lst(values, 2)}'
        )


@dataclass
class WeeklyDose:
    day_dose_mean: Collection[DailyAverageDose]

    @property
    def weekly_dose(self) -> Decimal:
        return sum(
            i.daily_dose 
            for i in self.day_dose_mean
        )
   
    def weekly_mean(self, key_val, num) -> Decimal:
        return sum(
            i.mean_lst(key_val, num)
            for i in self.day_dose_mean
        ) / 7
    
    @property
    def echo(self):
        print('\n'.join(i.str for i in self.day_dose_mean))
        print(f'Weekly dose -> {SUBSTANCE}: {self.weekly_dose} {UNIT}')
        print(f'Weekly dose -> mean: {self.weekly_mean(values, 2}')
        print(f'Weekly time -> mean: {self.weekly_mean(keys, 4)}')


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
