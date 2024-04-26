import json
from app import lambda_handler

def test_lambda_handler():
    event = {
        'requestContext': {
            'connectionId': 'test_connection_id',
            'eventType': 'MESSAGE'
        },
        'body': 'Test message'
    }

    response = lambda_handler(event, {})
    assert response['statusCode'] == 200