"""Demonstration of decorator pattern in Python (not demonstrating the language feature)"""

import abc
import re
from typing import Optional


class AbstractWindow(abc.ABC):
    """
    Describes a general window. Windows all have names and descriptions.
    """
    @property
    @abc.abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def describe_window(self) -> str:
        raise NotImplementedError


class ResidentialWindow(AbstractWindow):
    """
    The type of window that homes usually have.
    """
    @property
    def name(self) -> str:
        return camelcase_to_spaces(type(self).__name__)

    def describe_window(self) -> str:
        return 'This window is intended for balancing privacy with the need for light for those inside the building.'


class ShopWindow(AbstractWindow):
    """
    The type of window that shops usually have.
    """
    def __init__(self, name_of_shop: Optional[str] = None):
        self._name_of_shop = name_of_shop

    @property
    def name(self) -> str:
        if self._name_of_shop:
            return f'{self._name_of_shop} Window'

        return camelcase_to_spaces(type(self).__name__)

    def describe_window(self) -> str:
        return 'This window is intended for balancing security with enticing consumers to enter and stay inside the building.'


class CurtainDecorator(AbstractWindow):
    """Decorates any kind of window with fabric curtains."""

    def __init__(
            self,
            window: AbstractWindow,
            color: Optional[str] = None,
            open_status: Optional[bool] = None
        ):
        self._wrapped_window = window
        self._color = color
        self._open_status = open_status

    @property
    def name(self) -> str:
        return self._wrapped_window.name
    
    def describe_window(self) -> str:
        desc = self._wrapped_window.describe_window() + ' Upon peering inside, draped fabric is visible.'
        if self._color:
            desc += f' The fabric is a shade of {self._color}.'
        if self._open_status is not None:
            if self._open_status:
                desc += f' The two halves of fabric are pulled apart to reveal the interior of the room.'
            else:
                desc += f' The two halves of fabric are pulled together to obscure the view of the interior of the room.'
        return desc


class IronBarDecorator(AbstractWindow):
    def __init__(self, window: AbstractWindow):
        self._wrapped_window = window
    
    @property
    def name(self) -> str:
        return 'Scary ' + self._wrapped_window.name

    def describe_window(self) -> str:
        return self._wrapped_window.describe_window() + ' The outside of the window is guarded by imposing vertical iron bars, giving the impression of a formidable prison.'


class StuffedAnimalPalDecorator(AbstractWindow):
    def __init__(self, window: AbstractWindow):
        self._wrapped_window = window
    
    @property
    def name(self) -> str:
        return self._wrapped_window.name
    
    def describe_window(self) -> str:
        return self._wrapped_window.describe_window() + ' From inside, there is a stuffed animal propped on the window ledge, angled as though it is waving invitingly.'


class DynamicDescriptionDecorator(AbstractWindow):
    def __init__(self, window: AbstractWindow, custom_description: str, window_owner_name: Optional[str] = None):
        self._wrapped_window = window
        self._custom_description = custom_description
        self._window_owner_name = window_owner_name

    @property
    def name(self) -> str:
        if not self._window_owner_name:
            return self._wrapped_window.name
        return "{}'s {}".format(self._window_owner_name, self._wrapped_window.name)
    
    def describe_window(self) -> str:
        return self._wrapped_window.describe_window() + ' ' + self._custom_description


def camelcase_to_spaces(content: str) -> str:
    """
    Translate 'CamelCaseNames' to 'Camel Case Names'.
    Used when generating names from classes.
    (This regex was taken from Django Rest Framework view utils and the method slightly adapted.)
    (Yeah, I do avoid writing my own regex where possible, and I don't feel that bad about it.)
    """
    camelcase_boundary = '(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))'
    content = re.sub(camelcase_boundary, ' \\1', content).strip()
    return content[0].upper() + content[1:]


def print_window_name_and_desc(w):
        print('\t', w.name, ' | ', w.describe_window())


def main() -> None:
    print('Starting demonstration of decorator pattern.')

    windows = [ResidentialWindow(), ShopWindow(), ShopWindow('Candy Emporium')]
    print('Printing the basic names and descriptions of concrete window classes without decorators:')
    for w in windows:
        print_window_name_and_desc(w)

    print('Decorating a shop window in a scary neighborhood:')
    print_window_name_and_desc(IronBarDecorator(StuffedAnimalPalDecorator(ShopWindow())))

    print('Describing a cute little apartment window:')
    print_window_name_and_desc(
        CurtainDecorator(
            DynamicDescriptionDecorator(
                ResidentialWindow(),
                'This window has a small half-peeled sticker on it.',
                window_owner_name='Winona',
            ),
            color='red',
            open_status=True,
        )
    )

    print('Order of decoration can matter, depending on the operation. For this example, it does matter.')
    print_window_name_and_desc(
        DynamicDescriptionDecorator(
            CurtainDecorator(
                ResidentialWindow(),
                color='red',
                open_status=True,
            ),
            'This window has a small half-peeled sticker on it.',
            window_owner_name='Winona',
        )
    )

if __name__ == "__main__":
    main()
