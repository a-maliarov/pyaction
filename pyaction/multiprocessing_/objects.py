# -*- coding: utf-8 -*-

"""
pyaction.multiprocessing_.objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main objects of the multiprocessing field.

"""

__all__ = ['chunk']

#-----------------------------------------------------------------------------

def chunk(lst, parts):
    k, m = divmod(len(lst), parts)
    chunks = [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(parts)]
    return chunks

#-----------------------------------------------------------------------------
