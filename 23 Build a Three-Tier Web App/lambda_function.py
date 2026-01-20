import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1'
)

table = dynamodb.Table('UserData')


def lambda_handler(event, context):
    query_params = event.get('queryStringParameters') or {}
    user_id = query_params.get('userId')

    if not user_id:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'userId query parameter is required'})
        }

    try:
        response = table.get_item(
            Key={'userId': user_id}
        )

        item = response.get('Item')

        if item:
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps(item)
            }
        else:
            return {
                'statusCode': 404,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'message': 'No user data found'})
            }

    except ClientError as e:
        print("Unable to retrieve data:", e)
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Failed to retrieve user data'})
        }
