# -*- coding: utf-8 -*-

"""
pyaction.multiprocessing_.objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main objects of the multiprocessing field.

"""

__all__ = ['chunk']

#-----------------------------------------------------------------------------

def chunk(lst, parts):
    """
    Divides a list into specified number of sublists.

    Args:
        lst (list): The list to chunked.
        parts (int): The number of parts the list should be divided into.

    Returns:
        list: Chunked list.

    """

    k, m = divmod(len(lst), parts)
    chunks = [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(parts)]
    return chunks

#-----------------------------------------------------------------------------
