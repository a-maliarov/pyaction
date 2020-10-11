# -*- coding: utf-8 -*-

"""
pyaction
~~~~~~~~

PyAction is a module dedicated to eliminate rewriting the same code from
project to project by providing a set of tools according to specific python
fields.

Library hierarchy (this must be set and be followed in any case):
pyaction/
    field_name/
        __init__.py
        objects.py
        utils.py

Rules:
1. An __init__ file within a field folder should provide a short description
of the field and contain imports of the main objects within this field to be
operated by the end user.
2. The file called "objects.py" should contain all the main objects of the
field to be used by the end user.
3. he file called "utils.py" should contain all the utilities to be used by
the "objects.py" and not the end user.

"""

from .general import *

#-----------------------------------------------------------------------------
