"""This file implements fixtures for our tests"""

# flake8: noqa W293 E501
import os
import pytest
from tempfile import NamedTemporaryFile


@pytest.fixture
def temporary_file():
    """Temporary file Fixture."""
    # Creates a temporary file and returns its path
    with NamedTemporaryFile(delete=False, mode='w', newline='') as tmp_file:
        yield tmp_file.name
        if os.path.exists(tmp_file.name):
            os.remove(tmp_file.name)


@pytest.fixture
def test_data():
    """Test data Fixture."""
    # Creates a test data
    test_data = [
        {"id": 1, "nome": "Phone", "valor": 1500.0, "data_criacao": "2024-11-25", "electronico": True}
    ]

    return test_data