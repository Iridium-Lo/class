from _decimal import Decimal
from dataclasses import dataclass
from locale import currency, setlocale, LC_ALL
from sys import stdout
from typing import Collection

TAX = Decimal(0.15)


@dataclass
class Product:
    name: str
    price: Decimal

    @property
    def tax(self) -> Decimal:
        return TAX * self.price

    @property
    def price_with_tax(self) -> Decimal:
        return (1 + TAX) * self.price


@dataclass
class OrderedProduct:
    product: Product
    quantity: int

    @property
    def price(self) -> Decimal:
        return self.quantity * self.product.price

    @property
    def tax(self) -> Decimal:
        return self.quantity * self.product.tax

    @property
    def price_with_tax(self) -> Decimal:
        return self.quantity * self.product.price_with_tax

    def format_row(self) -> str:
        return (
            f'{self.product.name:10} '
            f'{currency(self.product.price):>6} '
            f'{self.quantity:>3} '
            f'{currency(self.tax):>6} '
            f'{currency(self.price_with_tax):>8}'
        )


@dataclass
class Order:
    products: Collection[OrderedProduct]

    @property
    def quantity(self) -> int:
        return sum(p.quantity for p in self.products)

    @property
    def tax(self) -> Decimal:
        return sum(p.tax for p in self.products)

    @property
    def price_with_tax(self) -> Decimal:
        return sum(p.price_with_tax for p in self.products)

    def print(self, f=stdout) -> None:
        print(f'{"Name":10} {"Price":>6} {"Qty":>3} {"Tax":>6} {"Subtotal":>8}', file=f)

        print('\n'.join(p.format_row() for p in self.products), file=f)

        print(
            f'{"TOTAL":10} '
            f'{"":>6} '
            f'{self.quantity:>3} '
            f'{currency(self.tax):>6} '
            f'{currency(self.price_with_tax):>8}',
            file=f,
        )


def main():
    setlocale(LC_ALL, '')

    order = Order(
        products=[
            OrderedProduct(
                product=Product(name='apple', price=Decimal(0.20)),
                quantity=16,
            ),
            OrderedProduct(
                product=Product(name='orange', price=Decimal(0.30)),
                quantity=20,
            )
        ],
    )
    order.print()


if __name__ == '__main__':
    main()
