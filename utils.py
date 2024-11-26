"""This file is where we create some utils funtions for our project"""

# flake8: noqa W293 E501

import os
import json
from datetime import datetime


def load_data(json_db_file_path: str):
    """
    Loads data from a JSON file,
    creating the file if it does not exist.

    This function manages data stored in a JSON file acting as a "database."
    If the specified file does not exist, 
    it creates the file with an empty list.
    It then reads and returns the data as a list of objects.

    Parameters:
        json_db_file_path (str): The path to the JSON file containing the data.

    Returns:
        list: A list of objects loaded from the JSON file.
            Returns an empty list if the file is empty or does not exist.
    
    Raises:
        json.JSONDecodeError: If the JSON file is corrupted or contains invalid format.
        OSError: If there is an error accessing or creating the file.
    """

    if not os.path.exists(json_db_file_path):
        # Create the file and initialize it with an empty list
        with open(json_db_file_path, 'w') as file:
            json.dump([], file)
    
    with open(json_db_file_path, 'r') as file:
        return json.load(file)
    
def assert_data_type(data: dict):
    """
    Verifies if the data of an item is in the correct format:
    - nome: str
    - valor: float
    - data_criacao: timestamp (datetime)
    - eletronico: bool
    
    Parameters:
        data (dict): The JSON object to be checked.
    
    Raises:
        ValueError: If any of the fields is in the wrong format.
    """
    if not isinstance(data.get("nome"), str):
        raise ValueError("Field 'Nome' must be a string")
    
    if not isinstance(data.get("valor"), float):
        raise ValueError("Field 'valor' must be a float")
    
    try:
        datetime.fromisoformat(data.get("data_criacao"))
    except ValueError:
        raise ValueError("Field 'creation_date' must be of type 'timestamp' (ISO 8601)")
    
    if not isinstance(data.get("eletronico"), bool):
        raise ValueError("Field 'eletronico' must be a bool")
    