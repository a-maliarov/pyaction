# -*- coding: utf-8 -*-

"""
pyaction.general.objects
~~~~~~~~~~~~~~~~~~~~~~~~

The main objects of the general field.

"""

__all__ = [
    'json_to_dict', 'dict_to_json', 'file_to_list', 'write_list_as_line'
]

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

    """

    with open(path_to_file, 'w', encoding=encoding) as js:
        json.dump(data, js)

def file_to_list(path_to_file, keep_duplicates=True, encoding='utf-8'):
    """Transforms a plain text (txt or csv) file to Python :obj:`list`.

    Args:
        path_to_file (str): A path to plain text file.
        keep_duplicates (bool): If set to False, the output list will not
            contain duplicates. Defaults to True.
        encoding (str): File's encoding. Defaults to "utf-8".

    Returns:
        list: The processed plain text file as a Python :obj:`list`.

    """

    handler = open(path_to_file, "r", encoding=encoding)
    lines = [line.replace("\n", "") for line in handler.readlines()]
    handler.close()

    return lines if keep_duplicates else list(dict.fromkeys(lines))

def write_list_as_line(path_to_file, data, delimiter=',', headers=False, encoding='utf-8'):
    """Writes Python :obj:`list` as a plain text line.

    Args:
        path_to_file (str): A path to output file.
        data (list): List to be stored.
        delimiter (str): Delimiter for the list elements.
        headers (bool): If set to True, the output line will overwrite
            the file. Defaults to False.
        encoding (str): File's encoding. Defaults to "utf-8".

    """

    mode = {0: 'a', 1: 'w'}
    data_to_write = [str(element) for element in data]

    handler = open(path_to_file, mode=mode[headers], encoding=encoding)
    handler.write(delimiter.join(data_to_write) + '\n')
    handler.close()

#-----------------------------------------------------------------------------
