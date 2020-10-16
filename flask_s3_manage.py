from flask import Flask , request
import boto3
from secrets import access_key, secret_key
from botocore.exceptions import ClientError
import logging

app = Flask(__name__)
client = boto3.client('s3', aws_access_key_id = access_key,aws_secret_access_key = secret_key)

@app.route('/',methods = ["GET"])
def home():
    return " Please use /api/v1/buckets to list all the S3 buckets "

@app.route('/api/v1/buckets',methods = ["GET"]) 
def get():
    bucket_list=[]
    bucket_dict = client.list_buckets()
    bucket_details = bucket_dict['Buckets']
    for bucket in bucket_details:
        bucket_list.append(bucket['Name'])
    return {'buckets' : bucket_list}

@app.route('/api/v1/delete',methods = ["GET"])
def delete():
    bucket_name = request.args.get('bucket')
    try:
        response = client.delete_bucket(Bucket=bucket_name)
    except:
        return "Please provide the correct bucket name!"
    return "{} bucket is deleted successfully".format(bucket_name)

@app.route('/api/v1/create',methods = ["GET"])
def create():
    session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    regions = session.get_available_regions('s3')
    bucket_name = request.args.get('bucket')
    region = request.args.get('region')
    if region in regions:
        try:
            client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=  {'LocationConstraint' : region})
            return "Bucket Creation is completed"
        except ClientError as e:
            print(e)
            if "location-constraint" in str(e):
                return "Please provide region name from selected regions!"
            else:
                return "Please provide a unique bucket name!"
    else:
        return "Please provide region name from the selected regions : af-south-1,ap-east-1,ap-northeast-1,ap-northeast-2,ap-south-1,ap-southeast-1,ap-southeast-2,ca-central-1,eu-central-1,eu-north-1,eu-west-1, eu-west-2,eu-west-3,sa-east-1,us-east-1,us-east-2,us-west-1,us-west-2"
  
if __name__ == '__main__': 
   app.run(debug=True,port=8080) 
