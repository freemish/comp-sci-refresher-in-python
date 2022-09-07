# Demonstrates iterator/iterable subclassing.

from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.
    """

    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: Iterable, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    Concrete Collections provide one or several methods for retrieving fresh
    iterator instances, compatible with the collection class.
    """
    _iter_reverse: bool = False

    def __init__(self, collection: List[Any] = [], iter_reverse: bool = False) -> None:
        self._collection = sorted(collection)
        self._iter_reverse = iter_reverse

    def __iter__(self) -> Iterator:
        return AlphabeticalOrderIterator(self._collection, self._iter_reverse)

    def set_iter_reverse(self, iter_reverse: bool) -> None:
        self._iter_reverse = iter_reverse

    def add_item(self, item: Any):
        self._collection.append(item)
        self._collection = sorted(self._collection)

    def __str__(self) -> str:
        return "{}<{}>".format(type(self).__name__, self._collection)


def main() -> None:
    print("Demonstrating iterator design pattern...")

    words_collection = WordsCollection(['nathan', 'molly', 'earl', 'lenny', 'sage', 'sophia', 'venus'])
    print(words_collection)
    words_collection.set_iter_reverse(True)
    for w in words_collection:
        print('\t', w)

    print("Adding a new item to collection and changing iterator...")
    words_collection.add_item('chia')
    words_collection.set_iter_reverse(False)
    for w in words_collection:
        print('\t', w)


if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/iterator.py
Demonstrating iterator design pattern...
WordsCollection<['earl', 'lenny', 'molly', 'nathan', 'sage', 'sophia', 'venus']>
         venus
         sophia
         sage
         nathan
         molly
         lenny
         earl
Adding a new item to collection and changing iterator...
         chia
         earl
         lenny
         molly
         nathan
         sage
         sophia
         venus
"""