# Demonstrates extension object pattern.

from abc import ABC, abstractmethod
from typing import Dict, Optional


class BaseExtension(ABC):
    is_auto_active: bool = True

    @abstractmethod
    def extend(self, word: str) -> str:
        raise NotImplementedError


class JustSomeClassThatDoesStuff:
    def __init__(self, some_word: str, extensions: Optional[Dict[str, BaseExtension]] = None):
        self._some_word = some_word
        self._extensions = extensions or {}

    def get_extension(self, name: str) -> Optional[BaseExtension]:
        return self._extensions.get(name)

    def add_extension(self, name: str, extension: BaseExtension) -> None:
        self._extensions[name] = extension
    
    def remove_extension(self, name: str) -> None:
        self._extensions.pop(name, None)
    
    def render(self) -> str:
        rendered_word = self._some_word
        for ext in self._extensions.values():
            if ext.is_auto_active:
                rendered_word = ext.extend(rendered_word)
        return rendered_word


class RepeatExtension(BaseExtension):
    def __init__(self, repeat_times: int = 2, is_auto_active: bool = True):
        self.repeat_times = repeat_times
        self.is_auto_active = is_auto_active

    def extend(self, word: str) -> str:
        return word * self.repeat_times


def main() -> None:
    print("Demonstrating extension object pattern (not very different from bridge?)...")
    some_class = JustSomeClassThatDoesStuff('molly')
    print('No extensions render:', some_class.render())

    some_class.add_extension('_repeater', RepeatExtension())
    some_class.add_extension('_triple_repeater', RepeatExtension(3))
    print('Some extensions render:', some_class.render())

    some_class.get_extension('_triple_repeater').is_auto_active = False
    print('Deactivate one extension temporarily:', some_class.render())

    some_class.add_extension('repeater', RepeatExtension(is_auto_active=False))
    print('Use an on-request extension:', some_class.get_extension('repeater').extend('ad-hoc'))


if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/extension_object.py
Demonstrating extension object pattern (not very different from bridge?)...
No extensions render: molly
Some extensions render: mollymollymollymollymollymolly
Deactivate one extension temporarily: mollymolly
Use an on-request extension: ad-hocad-hoc
"""