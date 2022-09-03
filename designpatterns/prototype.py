"""Demonstration of prototype pattern."""

from copy import deepcopy
from typing import Any, Dict, Optional


def get_object_attrs(obj: Optional[Any]) -> Dict:
    if not obj:
        return {}
    return {x: getattr(obj, x) for x in list(obj.__dir__()) if (not x.startswith('_') and not callable(getattr(obj, x)))}


class AbstractShape:
    def _set_kwarg(self, kwargs: Dict, attr: str, default_val: Optional[Any] = None) -> None:
        """If in kwargs, sets; else if set already, set that value; else, use default."""
        setattr(self, attr, kwargs.get(attr, getattr(self, attr, default_val)))

    def __init__(self, **kwargs):
        self._set_kwarg(kwargs, 'x', 0)
        self._set_kwarg(kwargs, 'y', 0)
        self._set_kwarg(kwargs, 'color')

    def clone(self) -> 'AbstractShape':
        return deepcopy(self)


class Rectangle(AbstractShape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._set_kwarg(kwargs, 'width', 0)
        self._set_kwarg(kwargs, 'height', 0)


class Circle(AbstractShape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._set_kwarg(kwargs, 'radius', 0)


def main() -> None:
    print("Demonstrates prototype pattern (which is available in Python out of the box with the copy module)...")

    circle = Circle(x=1, y=2, radius=3, color='red')
    print('original circle:', get_object_attrs(circle))

    clone_circle = circle.clone()
    print('cloned circle:', get_object_attrs(clone_circle))

    assert get_object_attrs(circle) == get_object_attrs(clone_circle)


if __name__ == '__main__':
    main()
