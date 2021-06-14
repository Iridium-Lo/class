from typing import Dict


class ConvertToKelvin:
    def __init__(self, substance: str, temp: Dict[str, float]):
        self.substance = substance
        self.temp = temp

    def to_kelvin(self, celsius: int) -> int:
        return celsius + 273

    def __str__(self):
        x = self.substance
        y = self.to_kelvin(self.temp["mp"])
        z = self.to_kelvin(self.temp["bp"])

        return f'{x}\n mp: {y}K\n bp: {z}K\n'


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
