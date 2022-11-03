"""
Demo for filter pattern, according to this site:
https://dzone.com/articles/using-filter-design-pattern-in-java#:~:text=The%20Filter%20Design%20Pattern%20is,criteria%20to%20obtain%20single%20criteria.
"""

import abc
from typing import List


class IFilterable(abc.ABC):
    pass


class Dog(IFilterable):
    def __init__(self, name: str, breed: str, gender: str):
        self.name = name
        self.breed = breed
        self.gender = gender

    def __str__(self) -> str:
        return '{} <name: {}; breed: {}; gender: {}>'.format(
            type(self).__name__, self.name, self.breed, self.gender
        )


class IFilter(abc.ABC):
    def apply(self, filterable_list: List[IFilterable]) -> List[IFilterable]:
        pass


class MalamuteFilter(IFilter):
    @staticmethod
    def apply(filterable_list: List[Dog]) -> List[Dog]:
        return [d for d in filterable_list if d.breed.lower() == 'malamute']


class MaleFilter(IFilter):
    @staticmethod
    def apply(filterable_list: List[Dog]) -> List[Dog]:
        return [d for d in filterable_list if 'm' in d.gender.lower()]


def main() -> None:
    dog_list = [
        Dog("Molly", "German Shepherd", "F"),
        Dog("Julie", "Rottweiler", "F"),
        Dog("Hank", "Golden Retriever", "M"),
        Dog("Chess", "Malamute", "M"),
        Dog("Tyrian", "French Bulldog", "M"),
        Dog("Angela", "Malamute", "F"),
    ]
    print("Original dog list:", [str(x) for x in dog_list])

    malamutes = MalamuteFilter.apply(dog_list)
    print("Malamute dog list:", [str(x) for x in malamutes])

    males = MaleFilter.apply(malamutes)
    print("Male malamute dog list:", [str(x) for x in males])


if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/filter.py 
Original dog list: ['Dog <name: Molly; breed: German Shepherd; gender: F>', 'Dog <name: Julie; breed: Rottweiler; gender: F>', 'Dog <name: Hank; breed: Golden Retriever; gender: M>', 'Dog <name: Chess; breed: Malamute; gender: M>', 'Dog <name: Tyrian; breed: French Bulldog; gender: M>', 'Dog <name: Angela; breed: Malamute; gender: F>']
Malamute dog list: ['Dog <name: Chess; breed: Malamute; gender: M>', 'Dog <name: Angela; breed: Malamute; gender: F>']
Male malamute dog list: ['Dog <name: Chess; breed: Malamute; gender: M>']
"""
