import os

TABLE_NAME = 'MachineManagement'
DEFAULT_REGION = 'us-west-1'
DEBUG = os.environ['DEBUG']
ENDPOINT = os.environ['DYNAMODB_ENDPOINT']
VALID_DOMAIN = os.environ['VALID_DOMAIN']
HASH_ALGORITHM = 'sha256'
