import json

# import requests

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'ChatMessages'

def lambda_handler(event, context):
    connection_id = event['requestContext']['connectionId']

    if event['requestContext']['eventType'] == 'CONNECT':
        # Handle new connection
        return {'statusCode': 200}

    elif event['requestContext']['eventType'] == 'DISCONNECT':
        # Handle disconnection
        return {'statusCode': 200}

    elif event['requestContext']['eventType'] == 'MESSAGE':
        # Handle incoming messages
        message = event['body']

        # Save message to DynamoDB
        table = dynamodb.Table(table_name)
        table.put_item(Item={'connectionId': connection_id, 'message': message})

        return {'statusCode': 200}


 #def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

     #return {
     #    "statusCode": 200,
      #   "body": json.dumps({
       #      "message": "hello world",
        #     # "location": ip.text.replace("\n", "")
         #}),
     #}
