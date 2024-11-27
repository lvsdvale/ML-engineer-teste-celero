"""This file implements test for auto_increment_id funcion"""

# flake8: noqa W293 E501

import json
import os
from utils import auto_increment_id
from fixtures import temporary_file, test_data  # noaq: F401


def test_auto_incremental_id_empty_data(temporary_file):
    """test if the funciton auto_increment_id corretly"""
    if os.path.exists(temporary_file):
        os.remove(temporary_file)
    
    new_id = auto_increment_id(temporary_file)

    assert new_id == 1, "id is not equal the next incremental id, must be 1"


def test_auto_incremental_id_with_data(temporary_file, test_data):
    """test if the funciton auto_increment_id corretly"""
    #create a file with 1 data
    with open(temporary_file, 'w') as tmp_file:
        json.dump(test_data, tmp_file)

    new_id = auto_increment_id(temporary_file)

    assert new_id == 2, "id is not equal the next incremental id, must be 2"
