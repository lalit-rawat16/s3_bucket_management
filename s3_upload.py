import boto3

from secrets import access_key, secret_key

import boto3
import os

#Connection to the S3 bucket
client = boto3.client('s3',aws_access_key_id = access_key,aws_secret_access_key = secret_key)

#Bucket name to upload
upload_file_bucket = 'lalitrawat16uploadbucket'

#Files upload count
file_count = 0

#Loop to upload all the python script in the current drectory
for file in os.listdir():
    if '.txt' in file:
        reply = str(input('Do you want to upload file {} (y/n):'.format(file))).lower().strip()
        if reply[0] == 'y': 
            client.upload_file(file, upload_file_bucket, file)
            print("{} file is successfully uploaded to the S3 bucket {}".format(file,upload_file_bucket))
            file_count += 1

#Check files uploaded
if file_count == 0:
    print("\nNo files are uploaded in the S3 bucket.")
elif file_count == 1 :
    print("\nFile uploaded in the S3 bucket is {}.".format(file_count))
else:
    print("\nFiles uploaded in the S3 bucket are {}.".format(file_count)))
