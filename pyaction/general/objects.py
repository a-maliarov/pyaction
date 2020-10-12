# -*- coding: utf-8 -*-

"""
pyaction.general.objects
~~~~~~~~~~~~~~~~~~~~~~~~

The main objects of the general field.

"""

__all__ = ['json_to_dict', 'dict_to_json', 'file_to_list']

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

def file_to_list(path_to_file, keep_duplicates=True, encoding='utf-8'):
    """Transforms a plain text (txt or csv) file to Python :obj:`list`.

    Args:
        path_to_file (str): A path to plain text file.
        encoding (str): File's encoding. Defaults to "utf-8".
        keep_duplicates (bool): If set to False, the output list will not
            contain duplicates. Defaults to True.

    Returns:
        list: The processed plain text file as a Python :obj:`list`.

    """

    handler = open(path_to_file, "r", encoding=encoding)
    lines = [line.replace("\n", "") for line in handler.readlines()]
    handler.close()

    return lines if keep_duplicates else list(dict.fromkeys(lines))

#-----------------------------------------------------------------------------
