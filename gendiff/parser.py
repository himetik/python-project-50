"""Parse files."""

import json
import pathlib

from yaml import CLoader as Loader
from yaml import load as yaml_load


def parse_json(json_data):
    """
    Parse json data.

    Args:
        json_data: json data for parsing

    Returns:
        dict
    """
    return json.load(json_data)


def parse_yaml(yaml_data):
    """
    Parse yaml data.

    Args:
        yaml_data: yaml data for parsing

    Returns:
        dict
    """
    return yaml_load(yaml_data, Loader=Loader)


def get_file_info(file_path):
    """
    Get absolute path and extension of the file.

    Args:
        file_path (str): file path

    Returns:
        tuple: (absolute path, file extension)
    """
    file_path_obj = pathlib.Path(file_path)
    file_abs_path = file_path_obj.resolve()
    file_extension = file_path_obj.suffix
    return file_abs_path, file_extension


def parse_file(file_path):
    """
    Parse json or yaml file.

    Args:

        file_path (str): file path

    Returns:
        dict

    """
    parsers = {
        '.json': parse_json,
        '.yml': parse_yaml,
        '.yaml': parse_yaml,
    }

    file_abs_path, file_extension = get_file_info(file_path)

    if file_extension not in parsers:
        raise ValueError(
            f'Unsupported file type: "{file_extension}". '
            f'Supported file types: {", ".join(parsers.keys())}'
        )

    with open(file_abs_path) as file_obj:
        return parsers[file_extension](file_obj)
