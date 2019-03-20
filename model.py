import config
import hashlib
import datetime

from aws_controller import get_boto3_resource

from botocore.exceptions import ClientError


DYNAMODB = 'dynamodb'


class User(object):

    def __init__(self):
        self.email = None
        self.family = None
        self.timestamp = None
        self.password = None
        self._resource = get_boto3_resource(
            DYNAMODB)
        self.table = self._resource.Table(config.TABLE_NAME)

    def __create_user(self):
        return self.table.put_item(
                Item={
                    'email': self.email,
                    'timestamp': '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
                    'password': self.password
                }
            )

    def __get_user(self):
        return self.table.get_item(
            Key={
                'email': self.email
            }
        )

    @staticmethod
    def __validate_email(email):
        return email.split('@')[1] == config.VALID_DOMAIN

    @staticmethod
    def __hash_password(password):
        return hashlib.pbkdf2_hmac(
            config.HASH_ALGORITHM,
            bytes(password, 'utf-8'),
            b'salt',
            100000)

    def get_user(self, email):
        if self.__validate_email(email):
            self.email = email
            try:
                return self.__get_user()
            except ClientError as e:
                print(e.response['Error']['Message'])

    def create_user(self, email, password, family):
        if self.__validate_email(email):
            self.email = email
            self.password = self.__hash_password(password)
            return self.__create_user()
        else:
            raise UserError


class UserError(Exception):
    pass
