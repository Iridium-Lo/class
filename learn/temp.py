from typing import Dict


class ConvertToKelvin:
    def __init__(self, substance: str, data: Dict[str, int]):
        self.substance = substance
        self.data = data

    def to_kelvin(self, celsius: int) -> int:
        return celsius + 273

    def __str__(self):
        sub = self.substance
        mp = self.to_kelvin(self.data["mp"])
        bp = self.to_kelvin(self.data["bp"])
        return f'{sub}:\n mp: {mp}K\n bp: {bp}K\n'


data = (
    ConvertToKelvin(
        'water',
        {
            'bp': 0,
            'mp': 100
        }
    ),
    ConvertToKelvin(
        'imaginary',
        {
           'bp': 30,
           'mp': 120
        }
    ),
)

print('\n'.join(str(i) for i in data))
