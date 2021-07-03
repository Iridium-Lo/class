from decimal import Decimal
from dataclasses import dataclass
from typing import List, Dict, Iterable, Collection

UNIT = 'u'
SUBSTANCE = 'phen'


@dataclass
class DayDoseMean:
    day: str
    time_dose: Dict[float, float]

    @property
    def doses(self) -> List[Decimal]:
        return [
            round(
                Decimal(i), 1
            ) for i in self.time_dose.values()
        ]

    @property
    def times(self) -> List[Decimal]:
        return [
            round(
                Decimal(i), 2
            ) for i in self.time_dose.keys()
        ]

    @property
    def daily_dose(self) -> Decimal:
        return sum(i for i in self.doses)

    @property
    def mean(self) -> Decimal:
        return self.daily_dose / len(self.doses)

    @property
    def diff(self) -> Iterable[Decimal]:
        return (
            abs(
                self.times[i] - self.times[i+1]
            ) for i in range(len(self.times) - 1)
        )

    @property
    def time_mean(self) -> Decimal:
        return sum(self.diff) / len(self.times)

    @property
    def prnt(self):
        return (
            f'{self.day}{":":4}'
            f'{self.daily_dose}{UNIT:4}'
            f'{self.mean}{self.time_mean:7}'
        )


@dataclass
class WeekDoseMean:
    week_dose_mean: Collection[DayDoseMean]

    @property
    def weekly_dose(self) -> Decimal:
        return sum(
            i.daily_dose
            for i in self.week_dose_mean
        )

    @property
    def weekly_mean(self) -> Decimal:
        return round(
            sum(
                i.mean
                for i in self.week_dose_mean
            ) / 7, 1
        )

    @property
    def weekly_time_mean(self) -> Decimal:
        return round(
            sum(
                i.time_mean
                for i in self.week_dose_mean
            ) / 7, 2
         )

    @property
    def echo(self):
        print(
            f'\n--------------------------\n'
            f'{"Day":7}{SUBSTANCE:7}{"dM":6}tM\n'
            f'--------------------------'
        )

        print('\n'.join(i.prnt for i in self.week_dose_mean))

        print(
            f'--------------------------\n'
            f'Weekly {"dM":4} -> mean: '
            f'{self.weekly_mean}\n'
            f'Weekly {"tM":4} -> mean: '
            f'{self.weekly_time_mean}\n'
            f'--------------------------\n'
            f'Weekly dose -> '
            f'{SUBSTANCE}: {self.weekly_dose}{UNIT}\n'
            f'--------------------------'
        )


def main():
    days = WeekDoseMean(
        week_dose_mean=(
            DayDoseMean(
                day='Mon',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Tue',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Wed',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Thu',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Fri',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Sat',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Sun',
                time_dose={
                  12: 2,
                  14: 2
                }
            )
        )
    )
    days.echo


if __name__ == '__main__':
    main()
