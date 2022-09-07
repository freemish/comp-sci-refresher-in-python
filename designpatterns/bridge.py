# Demonstrates bridge design pattern.

from abc import ABC, abstractmethod
from decimal import Decimal
from enum import Enum
from typing import List, Optional

BASE_BAGEL_COST = Decimal("2.25")


class BagelFlavor(Enum):
    SALT = 1
    BLACK_SESAME = 2
    WHITE_SESAME = 3
    ONION = 4
    GARLIC = 5

    def get_cost(self) -> Decimal:
        return {
            self.SALT: Decimal("0.05"),
            self.BLACK_SESAME: Decimal("0.05"),
            self.WHITE_SESAME: Decimal("0.05"),
            self.ONION: Decimal("0.1"),
            self.GARLIC: Decimal("0.1"),
        }.get(self)


class AbstractBagel(ABC):
    def __init__(self, flavors: Optional[List[BagelFlavor]] = None):
        self.set_flavors(flavors)

    def set_flavors(self, flavors: List[BagelFlavor]) -> None:
        self.flavors = flavors or []

    @abstractmethod
    def get_cost(self) -> Decimal:
        raise NotImplementedError


class BuildYourOwnBagel(AbstractBagel):
    def get_cost(self) -> Decimal:
        cost = BASE_BAGEL_COST
        for flavor in self.flavors:
            cost += flavor.get_cost()
        return cost


class SpecialDealBagel(BuildYourOwnBagel):
    def get_cost(self) -> Decimal:
        cost = super().get_cost()
        if BagelFlavor.BLACK_SESAME in self.flavors and BagelFlavor.WHITE_SESAME in self.flavors:
            cost -= BagelFlavor.WHITE_SESAME.get_cost()
        if BagelFlavor.ONION in self.flavors and BagelFlavor.GARLIC in self.flavors:
            cost -= BagelFlavor.GARLIC.get_cost()
        if not self.flavors:
            cost -= Decimal("0.5")
        return cost


def main() -> None:
    print("Demonstrating bridge design pattern...")
    print("Rather than using a single method to calculate \"if has ingredient, add to cost,\" this separates bagels from the costs of their components.")
    print()
    print("Cost of plain BuildYourOwnBagel:", format(BuildYourOwnBagel().get_cost(), '.2f'))
    print("Cost of plain SpecialDealBagel: {:.2f}".format(SpecialDealBagel().get_cost()))
    everything_flavors = [BagelFlavor.BLACK_SESAME, BagelFlavor.GARLIC, BagelFlavor.ONION, BagelFlavor.SALT, BagelFlavor.WHITE_SESAME]
    print("Cost of byob everything bagel: {:.2f}".format(BuildYourOwnBagel(everything_flavors).get_cost()))
    print("Cost of special deal everything bagel: {:.2f}".format(SpecialDealBagel(everything_flavors).get_cost()))


if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/bridge.py
Demonstrating bridge design pattern...
Rather than using a single method to calculate "if has ingredient, add to cost," this separates bagels from the costs of their components.

Cost of plain BuildYourOwnBagel: 2.25
Cost of plain SpecialDealBagel: 1.75
Cost of byob everything bagel: 2.60
Cost of special deal everything bagel: 2.45
"""
