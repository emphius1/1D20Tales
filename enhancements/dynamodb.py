```python
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class EnhancedDynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')

    def get_table(self, table_name):
        return self.dynamodb.Table(table_name)

    def advanced_query(self, table_name, filter_expression):
        table = self.get_table(table_name)
        response = table.scan(
            FilterExpression=filter_expression
        )
        return response['Items']

    def efficient_data_caching(self, table_name, key, value):
        table = self.get_table(table_name)
        try:
            response = table.get_item(Key={key: value})
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']

    def update_item(self, table_name, key, value, update_expression, expression_values):
        table = self.get_table(table_name)
        table.update_item(
            Key={key: value},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values
        )

    def delete_item(self, table_name, key, value):
        table = self.get_table(table_name)
        table.delete_item(
            Key={key: value}
        )
```