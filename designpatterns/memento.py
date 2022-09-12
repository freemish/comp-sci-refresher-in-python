# Demonstrates memento design pattern.
# Mostly from: https://refactoring.guru/design-patterns/memento/python/example#example-0

from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters
from typing import Optional


class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Originator():
    """
    The Originator holds some important state that may change over time.
    It defines a method for creating a memento with its state inside it and another method
    for restoring the state from it.
    """

    _state = None
    """
    For the sake of simplicity, the originator's state is stored inside a single
    variable.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        """
        The Originator's business logic may affect its internal state.
        Therefore, the client should backup the state before launching methods
        of the business logic via the save() method.
        """

        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Caretaker():
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento. It
    works with all mementos via the base Memento interface.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def load_save(self, index: Optional[int] = None) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop() if index is None else self._mementos.pop(index)
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


def main() -> None:
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.load_save()

    print("\nClient: Once more! Let's roll back to our original state.\n")
    caretaker.load_save(0)


if __name__ == "__main__":
    main()


"""
$ python3 designpatterns/memento.py 
Originator: My initial state is: Super-duper-super-puper-super.

Caretaker: Saving Originator's state...
Originator: I'm doing something important.
Originator: and my state has changed to: srlqQmSYtnMDjkHpbJORhcvWCeXiLK

Caretaker: Saving Originator's state...
Originator: I'm doing something important.
Originator: and my state has changed to: OYIxiJNeQtXyUCKaGWnPDSlvkTAobu

Caretaker: Saving Originator's state...
Originator: I'm doing something important.
Originator: and my state has changed to: VyquwCxoNbYsJickphelrKMUXHaOIG

Caretaker: Here's the list of mementos:
2022-09-12 11:14:23 / (Super-dup...)
2022-09-12 11:14:23 / (srlqQmSYt...)
2022-09-12 11:14:23 / (OYIxiJNeQ...)

Client: Now, let's rollback!

Caretaker: Restoring state to: 2022-09-12 11:14:23 / (OYIxiJNeQ...)
Originator: My state has changed to: OYIxiJNeQtXyUCKaGWnPDSlvkTAobu

Client: Once more! Let's roll back to our original state.

Caretaker: Restoring state to: 2022-09-12 11:14:23 / (Super-dup...)
Originator: My state has changed to: Super-duper-super-puper-super.
"""