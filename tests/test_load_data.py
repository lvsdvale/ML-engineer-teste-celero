"""This file runs test for load_data function"""

# flake8: noqa W293 E501

import os
import sys
import json
from fixtures import temporary_file, test_data  # noaq: F401

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PROJECT_DIR)

from utils import load_data  # noqa: E402



def test_load_data_creates_file(temporary_file):
    """Test if the temporary file was created corretly."""
    # remove temporary file if was already created.
    if os.path.exists(temporary_file):
        os.remove(temporary_file)

    data = load_data(temporary_file)

    # Verify if the file was created.
    assert os.path.exists(temporary_file), "File not created"

    # Verify if is a empty list
    assert data == [], "File must be empty"


def test_load_data_reads_existing_data(temporary_file, test_data):
    """Test if it was read correctly."""

    # Write data in temporary file
    with open(temporary_file, 'w') as file:
        json.dump(test_data, file)

    data = load_data(temporary_file)

    # Verify if the data in the temporary file was written correctly
    assert data == test_data, "Read data is not equal to written data"
