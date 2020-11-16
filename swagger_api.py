from flask import Flask
from flask_restplus import Api, Resource
from secrets import access_key, secret_key
import boto3

app = Flask(__name__)

client = boto3.client('s3', aws_access_key_id = access_key,aws_secret_access_key = secret_key)

api = Api(app, version='1.0', title='S3 Buckets', description='Manage your S3 Buckets using Flask Endpoints')
ns = api.namespace('HTTP Methods', description='HTTP Methods for the flask Endpoints')

@ns.route('/api/v1/buckets',methods = ["GET"])
class buckets(Resource):
    def get(self):
        bucket_list=[]
        try:
            bucket_dict = client.list_buckets()
            bucket_details = bucket_dict['Buckets']
            for bucket in bucket_details:
                bucket_list.append(bucket['Name'])
            return {'buckets' : bucket_list}
        except:
            return {"Error" : "Unable to connect AWS endpoint!"}, 500
    
if __name__ == '__main__':
    app.run(debug=True)
