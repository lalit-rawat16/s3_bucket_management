import boto3

from secrets import access_key, secret_key

import boto3
import os

client = boto3.client('s3',aws_access_key_id = access_key,aws_secret_access_key = secret_key)

for file in os.listdir():
    if '.py' in file:
        print(file)
        upload_file_bucket = 'lalitrawat16uploadbucket'
        client.upload_file(file, upload_file_bucket, file)
