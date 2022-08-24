import graphene
from graphene.test import Client
import pytest
from app.schema import Query, Mutations
from app.objectmgr import ObjectMgr
schema = graphene.Schema(query=Query, mutation=Mutations)

false = False
true = True

get_object_mutation = '''mutation{ getObject{ number ok } }'''
free_object_mutation = '''mutation{ freeObject(number:{}){ number ok } }'''
is_empty_query = '''{ isEmpty }'''
available_count_query = '''{ availableCount }'''

@pytest.fixture(autouse=True)
def reset_singletons():
  ObjectMgr._instances = {}

def test_available_count():
    client = Client(schema)
    executed = client.execute(available_count_query)
    assert executed == {
        'data': {
            'availableCount': 5
        }
    }

def test_is_empty():
    client = Client(schema)
    executed = client.execute(is_empty_query)
    assert executed == {
        'data': {
            "isEmpty": false
        }
    }

def test_get_all():
    client = Client(schema)

    executed = client.execute(get_object_mutation)
    assert executed == {
        'data': {
            "getObject": {
                "number": 1,
                "ok": true
            }
        }
    }

    executed = client.execute(available_count_query)
    assert executed == {
        'data': {
            'availableCount': 4
        }
    }

    executed = client.execute(get_object_mutation)
    assert executed == {
        'data': {
            "getObject": {
                "number": 2,
                "ok": true
            }
        }
    }
    executed = client.execute(available_count_query)
    assert executed == {
        'data': {
            'availableCount': 3
        }
    }

    executed = client.execute(get_object_mutation)
    assert executed == {
        'data': {
            "getObject": {
                "number": 3,
                "ok": true
            }
        }
    }
    executed = client.execute(available_count_query)
    assert executed == {
        'data': {
            'availableCount': 2
        }
    }

    executed = client.execute(get_object_mutation)
    assert executed == {
        'data': {
            "getObject": {
                "number": 4,
                "ok": true
            }
        }
    }
    executed = client.execute(available_count_query)
    assert executed == {
        'data': {
            'availableCount': 1
        }
    }

    executed = client.execute(get_object_mutation)
    assert executed == {
        'data': {
            "getObject": {
                "number": 5,
                "ok": true
            }
        }
    }
    executed = client.execute(available_count_query)
    assert executed == {
        'data': {
            'availableCount': 0
        }
    }

    executed = client.execute(is_empty_query)
    assert executed == {
        'data': {
            "isEmpty": true
        }
    }

    executed = client.execute(get_object_mutation)
    assert executed == {
        'data': {
            "getObject": {
                "number": 0,
                "ok": false
            }
        }
    }


