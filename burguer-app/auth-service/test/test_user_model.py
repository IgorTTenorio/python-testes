import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user_model import serialize_user

def test_serialize_user_complete():
    user = {
        "email": "teste@email.com",
        "name": "Teste",
        "address": "Rua Teste, 123",
        "role": "user"
    }

    result = serialize_user(user)

    expected = {
        "email": "teste@email.com",
        "name": "Teste",
        "address": "Rua Teste, 123",
        "role": "user"
    }

    assert result == expected

def test_serialize_user_incomplete():
    user = {
        "email": "teste@email.com",
    }

    result = serialize_user(user)

    expected = {
        "email": "teste@email.com",
        "name": "",
        "address": "",
        "role": "user"
    }

    assert result == expected

def test_serialize_user_empty():
    user = {}

    result = serialize_user(user)

    expected = {
        "email": None,
        "name": "",
        "address": "",
        "role": "user"
    }

    assert result == expected

def test_serialize_user_integ():
    with pytest.raises(AttributeError):
        serialize_user(12345)

def test_serialize_user_string():
    with pytest.raises(AttributeError):
        serialize_user("not a dick")
def test_serialize_user_lista():
    with pytest.raises(AttributeError):
        serialize_user([])    

def test_serialize_user_none(): 
    with pytest.raises(AttributeError):
        serialize_user(None)           

def test_serialize_user_inesperado():
    user = {
        "email": 123456,
        "name":["Nome Inesperado", "Outro Nome"],
        "address": {"rua": "123 Exemplo"},
        "role": True
        }
    resultado = serialize_user(user)    

    esperado = {
        "email": 123456,
        "name": ["Nome Inesperado", "Outro Nome"],
        "address": {"rua": "123 Exemplo"},
         'role': True
    }  
    assert resultado == esperado


def test_serialize_user_dict_none():
    user = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }
    resultado = serialize_user(user)

    esperado = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }

    assert resultado == esperado