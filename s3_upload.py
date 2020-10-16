import boto3

from secrets import access_key, secret_key

import boto3
import os

storage_class_list = ["STANDARD","STANDARD_IA","ONEZONE_IA","INTELLIGENT_TIERING","GLACIER","DEEP_ARCHIVE"]

#Connection to the S3 bucket
client = boto3.client('s3',aws_access_key_id = access_key,aws_secret_access_key = secret_key)

#Bucket name to upload
upload_file_bucket = 'lalitrawat16uploadbucket'

#Files upload count
file_count = 0

#Get the working directory from where the files need to uplaod
file_path=(input("Please provide the directory path from where to upload:")).strip()
print("Please provide the AWS storage class to be used ():")

for i in range(len(storage_class_list)):
    print(str(i+1) + ":" + storage_class_list[i])

choice = int(input("Enter your Choice: "))

if choice in range(1,6):
    storage_class = storage_class_list[choice-1]
else:
    print("Invalid input!")

try:
    os.chdir(file_path)
except OSError:
    print("Path provided by user is incorrect")
    exit()


#Loop to upload all the python script in the current drectory

for file in os.listdir():
    if '.txt' in file:
        reply = str(input('Do you want to upload file {} (y/n):'.format(file))).lower().strip()
        if reply[0] == 'y': 
            client.upload_file(file, upload_file_bucket, file, ExtraArgs={'ContentType': "text/html", 'ACL': "public-read", 'StorageClass': storage_class})
            print("{} file is successfully uploaded to the S3 bucket {}".format(file,upload_file_bucket))
            file_count += 1

#Check files uploaded
if file_count == 0:
    print("\nNo files are uploaded in the S3 bucket.")
elif file_count == 1 :
    print("\nFile uploaded in the S3 bucket is {}.".format(file_count))
else:
    print("\nFiles uploaded in the S3 bucket are {}.".format(file_count))
