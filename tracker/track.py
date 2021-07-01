import calendar as c
from datetime import time as t
from decimal import Decimal as dec
from dataclasses import dataclass
from typing import List, Dict, Decimal, Iterable, Collection

UNIT = 'u'
SUBSTANCE = 's'


@dataclass
class DayDose:
    day: int
    day_time_dose: Dict[float, float]

    def lst(self, key_val, num) -> List[Decimal]:
        return dec(
            round(
                list(
                    self.day_time_dose
                    .key_val()
                ), num
            )
        )
    
    @property
    def lsts(self) -> List[Decimal]:
        return(
            times = self.lst(keys, 4)
            doses = self.lst(values, 2)
        )

    @property
    def daily_dose(self) -> Decimal:
        return sum(i for i in self.lsts.doses)
    
    @property
    def prnt_daily(self):
        return f'{self.day}: {self.daily_dose}'


@dataclass
class Mean:
    Time_dose: Collection[DayDose]

    def diff(self, lst) -> Iterable[Decimal]:
        return (
            abs(
                self.lst[i] - self.lst[i+1]
            ) for i in enumerate(self.lst - 1)
        )

    def mean(self, lst) -> Decimal:
        return sum(
            i for i in self.diff(self.lst)
        ) / len(self.lst)
    
    @property
    def prnt(self):
        return (
            f'{self.day}: {self.daily_dose.prnt_daily}'
            f'Mtime: {self.mean(self.time_dose.lsts.times)}'
            f'Mdose: {self.mean(self.time_dose.lsts.doses)}'
        )


@dataclass
class WeeklyDose:
    day_dose_mean: Collection[mean]

    @property
    def weekly_dose(self) -> Decimal:
        return sum(
            i.daily_dose 
            for i in self.day_dose_mean
        )
   
    def weekly_mean(self, type) -> Decimal:
        return sum(
            i.mean(self.day_dose_mean.lst.type)
            for i in self.day_dose_mean
        ) / 7
    
    @property
    def echo(self):
        print('\n'.join(i.prnt for i in self.day_dose_mean))
        print(f'Weekly dose -> {SUBSTANCE}: {self.weekly_dose} {UNIT}')
        print(f'Weekly dose -> mean: {self.weekly_mean(doses)}')
        print(f'Weekly time -> mean: {self.weekly_mean(times)}')


def main():
   days = WeeklyDose(
       day_dose_mean=(
           Mean(
               DayDose(
                   day=c.MONDAY,
                   time_dose={
                     t(12): 1,
                     t(13): 1,
                   }
               )
           ),
           Mean(
               DayDose(
                   day=c.TUESDAY,
                   time_dose={
                     t(12): 2,
                     t(14): 2
                   }
               )
           )
       )
   )
   days.echo

if __name__ == '__main__':
    main()
