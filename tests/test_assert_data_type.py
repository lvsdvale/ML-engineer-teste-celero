"""This file test  if the funcion assert_data_type is working correctly"""

# flake8: noqa W293 E501

import os
import sys 
import pytest
from datetime import datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PROJECT_DIR)

from utils import assert_data_type


def test_assert_data_type_valid():
    """assert with a valid data"""
    valid_object = {
        "nome": "Celular",
        "valor": 1500.0,
        "data_criacao": "2024-11-25T00:00:00",
        "eletronico": True
    }

    assert_data_type(valid_object)

def test_assert_data_type_invalid_nome():
    """try with an invalid Nome"""
    invalid_object = {
        "nome": 1234, 
        "valor": 1500.0,
        "data_criacao": "2024-11-25T00:00:00",
        "eletronico": True
    }
    with pytest.raises(ValueError, match="Field 'Nome' must be a string"):
        assert_data_type(invalid_object)

def test_assert_data_type_invalid_valor():
    """try with an invalid valor"""
    invalid_object = {
        "nome": "Celular",
        "valor": "1500",  
        "data_criacao": "2024-11-25T00:00:00",
        "eletronico": True
    }
    with pytest.raises(ValueError, match="Field 'valor' must be a float"):
        assert_data_type(invalid_object)

def test_assert_data_type_invalid_eletronico():
    """try with an invalid valor"""
    invalid_object = {
        "nome": "Celular",
        "valor": 1500.0,  
        "data_criacao": "2024-11-25T00:00:00",
        "eletronico": "True"
    }
    with pytest.raises(ValueError, match="Field 'eletronico' must be a bool"):
        assert_data_type(invalid_object)
