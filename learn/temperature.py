from dataclasses import dataclass


@dataclass(frozen=True)
class Temperature:
    celsius: float

    @property
    def kelvin(self) -> float:
        return self.celsius + 273.15

    def __str__(self):
        return f'{self.kelvin} K'


@dataclass(frozen=True)
class Substance:
    name: str
    melt: Temperature
    boil: Temperature

    def __str__(self):
        return (
            f'{self.name}:\n'
            f' melt: {self.melt}\n'
            f' boil: {self.boil}\n'
        )


substances = (
    Substance(
        'water',
        Temperature(celsius=0),
        Temperature(celsius=100),
    ),
    Substance(
        '2-methylobenzenol (o-cresol)',
        Temperature(celsius=30),
        Temperature(celsius=191),
    ),
)

print('\n'.join(str(i) for i in substances))
