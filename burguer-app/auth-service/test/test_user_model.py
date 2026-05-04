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