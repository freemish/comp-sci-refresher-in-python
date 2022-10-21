from ast import Return
import os

IMPORT_MYSTERY_CLASS = os.environ.get("IMPORT_MYSTERY_CLASS")
print("in some_module init: import mystery class?", IMPORT_MYSTERY_CLASS)


def import_nested_class_from_module() -> None:
    from .MysteryClass import MysteryClass
    return MysteryClass


if IMPORT_MYSTERY_CLASS:
    MysteryClass = import_nested_class_from_module()
