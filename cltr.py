class DoseWeekday:
    def __init__(self, weekday: int, doses: Dict[time, float]):
        if not (0 <= weekday < len(calendar.day_name)):
            raise ValueError(f'{weekday} is not a valid weekday index')

        self.weekday, self.doses = weekday, doses

    @property
    def dose_total(self) -> float:
        return sum(self.doses.values())

    @property
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
