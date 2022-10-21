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


"""
$ python3 other/access_mystery_class.py 
in some_module init: import mystery class? None
inner molly demo
[printing modules...]
        sys
        builtins
        _frozen_importlib
        _imp
        _thread
        _warnings
        _weakref
        _io
        marshal
        posix
        _frozen_importlib_external
        time
        zipimport
        _codecs
        codecs
        encodings.aliases
        encodings
        encodings.utf_8
        _signal
        _abc
        abc
        io
        __main__
        _stat
        stat
        _collections_abc
        genericpath
        posixpath
        os.path
        os
        _sitebuiltins
        _distutils_hack
        site
        _ast
        itertools
        keyword
        _operator
        operator
        reprlib
        _collections
        collections
        types
        _functools
        functools
        contextlib
        enum
        ast
        some_module
        some_module.MysteryClass

[printing modules again...]
        sys
        builtins
        _frozen_importlib
        _imp
        _thread
        _warnings
        _weakref
        _io
        marshal
        posix
        _frozen_importlib_external
        time
        zipimport
        _codecs
        codecs
        encodings.aliases
        encodings
        encodings.utf_8
        _signal
        _abc
        abc
        io
        __main__
        _stat
        stat
        _collections_abc
        genericpath
        posixpath
        os.path
        os
        _sitebuiltins
        _distutils_hack
        site
        _ast
        itertools
        keyword
        _operator
        operator
        reprlib
        _collections
        collections
        types
        _functools
        functools
        contextlib
        enum
        ast
in some_module init: import mystery class? 1
inner molly demo
"""