from typing import Dict


class ConvertToKelvin:
    def __init__(self, substance: str, temp: Dict[str, int]):
        self.substance = substance
        self.temp = temp

    def to_kelvin(self, celsius: int) -> int:
        return celsius + 273

    def __str__(self):
        sub = self.substance
        mp = self.to_kelvin(self.temp["mp"])
        bp = self.to_kelvin(self.temp["bp"])

        return f'{sub}:\n mp: {mp}K\n bp: {bp}K\n'


mp_bp_celsius = (
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

print('\n'.join(str(i) for i in mp_bp_celsius))
