from _decimal import Decimal
from dataclasses import dataclass
from typing import Collection


@dataclass
class Product:
    name: str
    price: Decimal
    qty: Decimal
	
    @property
    def round(self) -> Decimal:
        return round(self.price, 2)
    
    @property
    def unit_price(self) -> Decimal:
        return round(1 / self.qty * self.round, 2)
	
    @property
    def format_row(self) -> str:
        return (
            f'{self.name}'
            f'{"£":>4}{self.round}'
            f'{self.qty:>4}'
            f'{"£":>6}{self.unit_price}'
        )


@dataclass
class Order:
    products: Collection[Product]

    @property
    def total(self) -> Decimal:
        return sum(i.round for i in self.products)

    @property
    def echo(self):
        print(f'name{"price:":>8}{"qty:":>6}{"unit:":>7}')
        print('\n'.join(i.format_row for i in self.products))
        print(f'\nT -> {"£":>1}{self.total:}')
	

def main():
    cosmetics = Order(
        products=[
            Product(
                name='saly', price=Decimal(6.99), qty=Decimal(1)
            ),
            Product(
                name='koji', price=Decimal(7.99), qty=Decimal(1)
            ),
            Product(
                name='jojo', price=Decimal(7.45), qty=Decimal(1)
            ),
            Product(
                name='glyo', price=Decimal(9.99), qty=Decimal(1)
            ),
            Product(
                name='band', price=Decimal(6.95), qty=Decimal(1)
            )
        ],
    )
    cosmetics.echo

if __name__ == '__main__':
    main()
