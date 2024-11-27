"""This file implements tests for save_data funcion"""

# flake8: noqa W293 E501

import json
from utils import save_data
from fixtures import temporary_file, test_data # noaq: F401


def test_save_data(temporary_file, test_data):
    """test if the funciton save_data saves corretly"""
    save_data(temporary_file, test_data)

    with open(temporary_file, 'r') as tmp_file:
        saved_data = json.load(tmp_file)

    #verify if the saved data has the same values as fixtures
    assert len(saved_data) == 1 
    assert saved_data[0]["nome"] == "Phone"
