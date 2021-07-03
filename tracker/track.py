import calendar as c
from decimal import Decimal
from dataclasses import dataclass
from typing import List, Dict, Iterable, Collection

UNIT = 'u'
SUBSTANCE = 'phen'


@dataclass
class DailyDose:
    day: int
    time_dose: Dict[float, float]

    @property
    def doses(self) -> List[Decimal]:
        return [
            round(
                Decimal(i), 2
            ) for i in self.time_dose.values()
        ]

    @property
    def daily_dose(self) -> Decimal:
        return sum(i for i in self.doses)

    @property
    def mean(self) -> Decimal:
        return self.daily_dose / len(self.doses)

    @property
    def prnt_daily(self):
        return (
            f'{c.day_name[self.day]}: {self.daily_dose}{UNIT} '
            f'{self.mean}'
        )


@dataclass
class Mean:
    daily_dose: Collection[DailyDose]

    @property
    def times(self) -> List[Decimal]:
        return [
            round(
                Decimal(i), 4
            ) for i in self.daily_dose.time_dose.keys()
        ]

    @property
    def diff(self) -> Iterable[Decimal]:
        return (
            abs(
                self.times[i] - self.times[i+1]
            ) for i in range(len(self.times) - 1)
        )

    @property
    def mean(self) -> Decimal:
        return sum(self.diff) / len(self.times)

    @property
    def prnt(self):
        return (
            f'{self.daily_dose.prnt_daily} '
            f'{self.mean} '
        )


@dataclass
class WeeklyDoseMean:
    day_dose_mean: Collection[Mean]

    @property
    def weekly_dose(self) -> Decimal:
        return sum(
            i.daily_dose
            for i in self.day_dose_mean
        )

    def weekly_mean(self, lst) -> Decimal:
        return sum(
            i.mean(lst)
            for i in self.day_dose_mean
        ) / 7

    @property
    def echo(self):
        print(f'{"Day":8} {SUBSTANCE:}  {"dM"}   tM')
        print('\n'.join(i.prnt for i in self.day_dose_mean))

      #  print(
           # f'Weekly time -> mean: {self.weekly_mean(self.day_dose_mean.daily_dose.times)}'
           # f'Weekly dose -> mean: {self.weekly_mean(self.day_dose_mean.daily_dose.doses)}'
           # f'Weekly dose -> {SUBSTANCE}: {self.weekly_dose} {UNIT}'
      #  )


def main():
    days = WeeklyDoseMean(
        day_dose_mean=(
            Mean(
                DailyDose(
                    day=c.MONDAY,
                    time_dose={
                      12: 1,
                      13: 1,
                    }
                )
            ),
            Mean(
                DailyDose(
                    day=c.TUESDAY,
                    time_dose={
                      12: 2,
                      14: 2
                    }
                )
            )
        )
    )
    days.echo


if __name__ == '__main__':
    main()
