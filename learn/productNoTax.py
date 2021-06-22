from _decimal import Decimal
from dataclasses import dataclass
from sys import stdout
from typing import Collection


@dataclass
class Product:
    name: str
    price: int

    @property
    def round(self) -> Decimal:
        return round(self.price, 2)

    @property
    def format_row(self) -> str:
        return (
            f'{self.name:10} '
            f'{self.round} '
        )


@dataclass
class Order:
    products: Collection[Product]

    @property
    def total(self) -> Decimal:
        return sum(i.round for i in self.products)

    def print(self, f=stdout) -> None:
        print('\n'.join(p.format_row for p in self.products))
        print(f'\ntotal {self.total:10}')


def main():
    order = Order(
        products=[
            Product(
                name='saly', price=Decimal(6.99)
            ),
            Product(
                name='kojic', price=Decimal(7.99)
            ),
            Product(
                name='jojoba', price=Decimal(7.45)
            ),
            Product(
                name='gylcol', price=Decimal(9.99)
            ),
            Product(
                name='jojoba', price=Decimal(7.45)
            ),
            Product(
                name='bandage', price=Decimal(6.95)
            )
        ],
    )
    order.print()


if __name__ == '__main__':
    main()
