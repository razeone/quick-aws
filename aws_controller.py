import boto3

import config


def create_table():

    dynamodb = get_boto3_resource('dynamodb')

    table = dynamodb.create_table(
        TableName=config.TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': 'email',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'timestamp',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'email',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'timestamp',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table


def get_boto3_resource(resource_name, **kwargs):
    if config.DEBUG:
        kwargs['endpoint_url'] = config.ENDPOINT
    return boto3.resource(resource_name, region_name=config.DEFAULT_REGION, **kwargs)
