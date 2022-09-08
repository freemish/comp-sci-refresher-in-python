# Demonstrates chain of responsibility pattern.

from abc import abstractmethod
from typing import Any, Optional


class BaseHandler:
    _next_handler: Optional['BaseHandler'] = None
    _do_next_handler_before_run: bool = False

    def set_next(self, handler: 'BaseHandler', do_next_handler_before_run: bool = False) -> 'BaseHandler':
        print('Setting next on {} with next handler {}'.format(type(self).__name__, type(handler).__name__))
        self._next_handler = handler
        self._do_next_handler_before_run = do_next_handler_before_run
        return handler

    def _pass_to_next_handler(self, request: Any) -> Optional[Any]:
        if self._next_handler:
            return self._next_handler.handle(request)

    @abstractmethod
    def run(self, request: Any) -> Optional[Any]:
        pass

    def handle(self, request: Any) -> Optional[Any]:
        print('{}: Request input: {}'.format(type(self).__name__, request))

        if self._do_next_handler_before_run:
            return self._pass_to_next_handler(request) or self.run(request)

        return self.run(request) or self._pass_to_next_handler(request)


class NullRequestHandler(BaseHandler):
    def run(self, request: Any) -> Optional[Any]:
        if request is None:
            return 'Request is None'


class FalsyRequestHandler(BaseHandler):
    def run(self, request: Any) -> Optional[Any]:
        if not request:
            return 'Request is falsy'


class ListRequestHandler(BaseHandler):
    def run(self, request: Any) -> Optional[Any]:
        if isinstance(request, list):
            return f'Request is a list: {request}'


class FlimsyAuthHandler(BaseHandler):
    def run(self, request: Any) -> Optional[Any]:
        allowed_substrings = ['good', 'happy', 'reasonable']
        passed = False
        for substr in allowed_substrings:
            if substr in str(request):
                passed = True

        if not passed:
            return 'Request did not pass fake authentication'


class CatchallHandler(BaseHandler):
    _do_next_handler_before_run: bool = True

    def run(self, _: Any) -> Optional[Any]:
        return 'Request passed all checks'


def main() -> None:
    print("Demonstrating chain of responsibility pattern...")

    handler_chain_1 = NullRequestHandler()
    handler_chain_1.set_next(ListRequestHandler()).set_next(CatchallHandler())
    handler_chain_2 = FalsyRequestHandler()
    handler_chain_2.set_next(FlimsyAuthHandler()).set_next(CatchallHandler())
    handler_chain_3 = FlimsyAuthHandler()

    print('handler chain start:', type(handler_chain_1).__name__)

    print('OUTPUT:', handler_chain_1.handle(['goodness']))
    print('OUTPUT:', handler_chain_2.handle(['goodness']))
    print('OUTPUT:', handler_chain_3.handle(None))


if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/chain_of_responsibility.py
Demonstrating chain of responsibility pattern...
Setting next on NullRequestHandler with next handler ListRequestHandler
Setting next on ListRequestHandler with next handler CatchallHandler
Setting next on FalsyRequestHandler with next handler FlimsyAuthHandler
Setting next on FlimsyAuthHandler with next handler CatchallHandler
handler chain start: NullRequestHandler
NullRequestHandler: Request input: ['goodness']
ListRequestHandler: Request input: ['goodness']
OUTPUT: Request is a list: ['goodness']
FalsyRequestHandler: Request input: ['goodness']
FlimsyAuthHandler: Request input: ['goodness']
CatchallHandler: Request input: ['goodness']
OUTPUT: Request passed all checks
FlimsyAuthHandler: Request input: None
OUTPUT: Request did not pass fake authentication
"""
