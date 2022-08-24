import graphene
from graphene.test import Client
from app.schema import Query, Mutations
schema = graphene.Schema(query=Query, mutation=Mutations)
false = False

def test_available_count():
    client = Client(schema)
    executed = client.execute('''{ availableCount }''')
    assert executed == {
        'data': {
            'availableCount': 5
        }
    }

def test_is_empty():
    client = Client(schema)
    executed = client.execute('''{ isEmpty }''')
    assert executed == {
        'data': {
            "isEmpty": false
        }
    }

def test_is_empty():
    client = Client(schema)
    executed = client.execute('''{ isEmpty }''')
    assert executed == {
        'data': {
            "isEmpty": false
        }
    }