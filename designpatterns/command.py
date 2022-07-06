"""Demonstration of command pattern."""

from abc import ABC, abstractmethod
from typing import Optional


class ImaginaryServiceClient:
    """Pretends to reach out to some imaginary service."""

    def log_command_action(self, command_action: str) -> None:
        print(f"Just logging a command action: {command_action}")


class AbstractCommand(ABC):
    """
    The AbstractCommand interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(AbstractCommand):
    """
    Some commands can implement simple operations on their own
    and don't reach into other receiver classes.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Basic print method! ({self._payload})")


class ComplexCommand(AbstractCommand):
    """
    However, some commands delegate more complex operations to other
    objects ("receivers").
    """

    def __init__(self, receiver: ImaginaryServiceClient) -> None:
        self._receiver = receiver
        self._command_action = "complex_command"

    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object")
        self._receiver.log_command_action(self._command_action)


class Invoker:
    """
    An Invoker sends requests to one or more commands.
    There could be multiple different invokers for the same business action,
    e.g. a button located in one place and a menu item link in another place.

    Storing the setup/teardown commands (which store their own parameters)
    allows for replay of commands.
    """

    _on_setup = None
    _on_teardown = None

    def __init__(
            self,
            on_setup_command: Optional[AbstractCommand] = None,
            on_teardown_command: Optional[AbstractCommand] = None,
        ):
        self.set_on_setup_command(on_setup_command)
        self.set_on_teardown_command(on_teardown_command)

    def set_on_setup_command(self, command: Optional[AbstractCommand]):
        self._on_setup = command

    def set_on_teardown_command(self, command: Optional[AbstractCommand]):
        self._on_teardown = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """

        print("Invoker: About to execute a start command, if any")
        if isinstance(self._on_setup, AbstractCommand):
            self._on_setup.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: About to execute finish command, if any")
        if isinstance(self._on_teardown, AbstractCommand):
            self._on_teardown.execute()


def main() -> None:
    print('Starting demonstration of command pattern...')

    print('\nStarting invoker without any special commands to wrap action...')
    invoker = Invoker()
    invoker.do_something_important()

    print('\nStarting invoker with startup and teardown commands...')
    invoker = Invoker(ComplexCommand(ImaginaryServiceClient()), SimpleCommand('Simple payload'))
    invoker.do_something_important()


if __name__ == '__main__':
    main()

"""
$ python3 designpatterns/command.py
Starting demonstration of command pattern...

Starting invoker without any special commands to wrap action...
Invoker: About to execute a start command, if any
Invoker: ...doing something really important...
Invoker: About to execute finish command, if any

Starting invoker with startup and teardown commands...
Invoker: About to execute a start command, if any
ComplexCommand: Complex stuff should be done by a receiver object
Just logging a command action: complex_command
Invoker: ...doing something really important...
Invoker: About to execute finish command, if any
SimpleCommand: Basic print method! (Simple payload)
"""
