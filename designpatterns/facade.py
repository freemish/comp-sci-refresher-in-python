# Demonstrates facade design pattern.
# See original source (only minor tweaks made): https://refactoring.guru/design-patterns/facade/python/example#example-0


class Facade:
    """
    The Facade class provides a simple interface to the complex logic of one or
    several subsystems.
    """

    def __init__(self, subsystem1: 'Subsystem1' = None, subsystem2: 'Subsystem2' = None):
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems at the cost of the many possible combinations
        and orders of calls that can be made to the managed subsystems.
        """

        results = []
        results.append("Facade calls subsystems' operation1:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform some action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def main() -> None:
    ss2 = Subsystem2()
    print(ss2.operation1())
    facade = Facade(subsystem2=ss2)
    print(facade.operation())


if __name__ == "__main__":
    main()


"""
$ python3 designpatterns/facade.py
Subsystem2: Get ready!
Facade calls subsystems' operation1:
Subsystem1: Ready!
Subsystem2: Get ready!
Facade orders subsystems to perform some action:
Subsystem1: Go!
Subsystem2: Fire!
"""
