# Demonstrates visitor pattern.

from enum import Enum
from typing import List


class InsuranceType(Enum):
    LIFE = 'life'
    HEALTH = 'health'
    THEFT = 'theft'
    RENTAL = 'rental'
    FIRE = 'fire'
    FLOOD = 'flood'


class InsuranceSalesman:
    def visit_residence(self) -> List[InsuranceType]:
        valid_types = [InsuranceType.HEALTH, InsuranceType.LIFE]
        return valid_types

    def visit_apartment(self) -> List[InsuranceType]:
        return [InsuranceType.RENTAL]

    def visit_business(self) -> List[InsuranceType]:
        return [InsuranceType.FIRE, InsuranceType.FLOOD, InsuranceType.THEFT]


class Insureable:
    def accept(self, insurance_salesman: InsuranceSalesman) -> List[InsuranceType]:
        pass


class Bank(Insureable):
    def accept(self, insurance_salesman: InsuranceSalesman) -> List[InsuranceType]:
        return insurance_salesman.visit_business()


class ApartmentLessee(Insureable):
    def accept(self, insurance_salesman: InsuranceSalesman) -> List[InsuranceType]:
        return insurance_salesman.visit_apartment()


class BusinessSpaceLessee(Insureable):
    def accept(self, insurance_salesman: InsuranceSalesman) -> List[InsuranceType]:
        return insurance_salesman.visit_apartment() + insurance_salesman.visit_business()


def main() -> None:
    print("Demonstrating visitor pattern...")

    salesman = InsuranceSalesman()
    potential_clients: Insureable = [Bank(), ApartmentLessee(), BusinessSpaceLessee(), ApartmentLessee()]
    for pc in potential_clients:
        print(type(pc).__name__, pc.accept(salesman))


if __name__ == '__main__':
    main()


"""
 python3 designpatterns/visitor.py
Demonstrating visitor pattern...
Bank [<InsuranceType.FIRE: 'fire'>, <InsuranceType.FLOOD: 'flood'>, <InsuranceType.THEFT: 'theft'>]
ApartmentLessee [<InsuranceType.RENTAL: 'rental'>]
BusinessSpaceLessee [<InsuranceType.RENTAL: 'rental'>, <InsuranceType.FIRE: 'fire'>, <InsuranceType.FLOOD: 'flood'>, <InsuranceType.THEFT: 'theft'>]
ApartmentLessee [<InsuranceType.RENTAL: 'rental'>]
"""
