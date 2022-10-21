import os
from sys import modules

from some_module import MysteryClass

print(MysteryClass.MysteryClass.InnerMysteryClass.inner)
print("[printing modules...]")
print("\t" + "\n\t".join(list(modules.keys())))

modules.pop("some_module.MysteryClass")
modules.pop("some_module")

print("\n[printing modules again...]")
print("\t" + "\n\t".join(list(modules.keys())))

os.environ["IMPORT_MYSTERY_CLASS"] = "1"
from some_module import MysteryClass

print(MysteryClass.InnerMysteryClass.inner)
