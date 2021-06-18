import calendar
from typing import Dict
from datetime import time

UNIT = 'u'
SUBSTANCE = 's'


class DoseWeekday:
    def __init__(self, weekday: int, doses: Dict[time, float]):
        self.doses = doses
        self.weekday = weekday

#//    @property
    def dose_total(self) -> float:
        return sum(self.doses.values())

#    @property
    def weekday_name(self) -> str:
        return calendar.day_name[self.weekday]

    def __str__(self):
        return f'{self.weekday_name}: {self.dose_total} {UNIT}'


days = (
   DoseWeekday(
       calendar.MONDAY,
       {
           time(12): 1,
           time(14): 3,
           time(16): 5,
       },
   ),
   DoseWeekday(
       calendar.TUESDAY,
       {
           time(12): 2,
           time(14): 2,
           time(16): 1,
       },
   ),
)

print('\n'.join(str(day) for day in days))
total_dose = sum(day.dose_total for day in days)
print(f'\nTotal -> {SUBSTANCE}: {total_dose} {UNIT}')
