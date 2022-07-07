"""Demonstration of builder pattern."""

import abc


class IceCreamSandwich:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient: str) -> None:
        self.ingredients.append(ingredient)

    def list_ingredients(self) -> str:
        return f"{', '.join(self.ingredients)}"

    def __str__(self) -> str:
        return f'IceCreamSandwich: Ingredients: {self.list_ingredients()}'


class Brownie:
    def __init__(self):
        self._cook_time = 0
        self._cook_temp_f = 0.0
        self.ingredients = []

        self._warm = False
        self._fluffy = False
        self._cooked = False
        self._burned = False

    def add_ingredient(self, ingredient: str) -> None:
        self.ingredients.append(ingredient)

    def cook(self) -> None:
        if self._cook_time > 5*60 and self._cook_temp_f > 200:
            self._warm = True
            if self._cook_time >= 10*60 and self._cook_temp_f >= 350:
                self._cooked = True
            if self._cook_time > 20*60 or self._cook_temp_f > 400:
                self._burned = True
            if not self._burned and 'egg' in self.ingredients:
                self._fluffy = True

    def is_tasty(self) -> bool:
        return (
            self._cooked
            and self._warm
            and self._fluffy
            and (not self._burned)
            and 'chocolate' in self.ingredients
        )

    def list_ingredients(self) -> str:
        return f"{', '.join(self.ingredients)}"

    def __str__(self) -> str:
        return 'Brownie: Ingredients: {}, Is Tasty? {}'.format(self.list_ingredients(), self.is_tasty())

    @property
    def cook_time(self) -> int:
        return self._cook_time

    @cook_time.setter
    def cook_time(self, cook_time: int) -> None:
        self._cook_time = cook_time

    @property
    def cook_temp_f(self) -> float:
        return self._cook_temp_f

    @cook_temp_f.setter
    def cook_temp_f(self, cook_temp_f: float) -> None:
        self._cook_temp_f = cook_temp_f


class AbstractTreatBuilder(abc.ABC):
    @abc.abstractmethod
    def get_treat(self):
        raise NotImplementedError

    @abc.abstractmethod
    def cook(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def mix_in_all_ingredients(self) -> None:
        raise NotImplementedError


class BrownieBuilder:
    def __init__(self):
        self._brownie = Brownie()
        self.all_ingredients = ['egg', 'flour',
                                'cocoa', 'chocolate', 'baking powder']
        self.cook_time_secs = 12*60
        self.cook_temp_f = 350

    def get_treat(self):
        return self._brownie

    def mix_in_all_ingredients(self):
        for ing in self.all_ingredients:
            self._brownie.add_ingredient(ing)

    def cook(self):
        self._brownie.cook_time = self.cook_time_secs
        self._brownie.cook_temp_f = self.cook_temp_f
        self._brownie.cook()


class IceCreamSandwichBuilder:
    def __init__(self):
        self._ics = IceCreamSandwich()
        self.all_ingredients = ['cookie', 'ice cream', 'cookie']

    def get_treat(self):
        return self._ics

    def mix_in_all_ingredients(self) -> None:
        for ing in self.all_ingredients:
            self._ics.add_ingredient(ing)

    def cook(self) -> None:
        return None


def get_builder(treat_name: str):
    return {
        'brownie': BrownieBuilder,
        'ice cream sandwich': IceCreamSandwichBuilder,
    }.get(treat_name)()


def main() -> None:
    print("Demonstrates builder pattern (and I guess a simple factory method too)...")

    print('Building an ice cream sandwich with no ingredients...')
    builder = get_builder('ice cream sandwich')
    print(builder.get_treat())

    print('Now an ice cream sandwich with ingredients mixed in and cooked:')
    builder.mix_in_all_ingredients()
    builder.cook()
    print(builder.get_treat())

    print('Now a brownie, raw, but with ingredients:')
    builder = get_builder('brownie')
    builder.mix_in_all_ingredients()
    print(builder.get_treat())

    print('Now cooked...')
    builder.cook()
    print(builder.get_treat())


if __name__ == '__main__':
    main()

"""
$ python3 designpatterns/builder.py
Demonstrates builder pattern (and I guess a simple factory method too)...
Building an ice cream sandwich with no ingredients...
IceCreamSandwich: Ingredients: 
Now an ice cream sandwich with ingredients mixed in and cooked:
IceCreamSandwich: Ingredients: cookie, ice cream, cookie
Now a brownie, raw, but with ingredients:
Brownie: Ingredients: egg, flour, cocoa, chocolate, baking powder, Is Tasty? False
Now cooked...
Brownie: Ingredients: egg, flour, cocoa, chocolate, baking powder, Is Tasty? True
"""
