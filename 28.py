import boto3

session = boto3.Session(profile_name='me')
client = session.client('iam')

paginator = client.get_paginator('list_users')
for response in paginator.paginate():
    print(response)
