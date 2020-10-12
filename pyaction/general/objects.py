# -*- coding: utf-8 -*-

"""
pyaction.general.objects
~~~~~~~~~~~~~~~~~~~~~~~~

The main objects of the general field.

"""

__all__ = ['json_to_dict', 'dict_to_json']

import json

#-----------------------------------------------------------------------------

def json_to_dict(path_to_file, encoding='utf-8'):
    """Transforms a file with ".json" format to Python :obj:`dict`.

    Args:
        path_to_file (str): A path to JSON file.
        encoding (str): File's encoding. Defaults to "utf-8".

    Returns:
        dict: The processed JSON file as a Python :obj:`dict`.

    """

    with open(path_to_file, 'r', encoding=encoding) as js:
        return json.loads(js.read())

def dict_to_json(path_to_file, data, encoding='utf-8'):
    """Saves a :obj:`dict` into a file with ".json" format.

    Args:
        path_to_file (str): A path to JSON file.
        data(dict): Dictionary to be stored.
        encoding (str): File's encoding. Defaults to "utf-8".

    Returns:
        dict: The processed JSON file as a Python :obj:`dict`.

    """

    with open(path_to_file, 'w', encoding=encoding) as js:
        json.dump(data, js)

#-----------------------------------------------------------------------------
