import boto3
import io
from datetime import datetime
import json

def store_in_s3(data, bucket_name, object_name):
    """
    Uploads any data as a file to an S3 bucket.
    
    Args:
    - data: The data to be uploaded (can be a dict for JSON or plain text).
    - bucket_name: The name of the S3 bucket.
    - object_name: The name of the object to be stored in the S3 bucket.
    """
    s3_client = boto3.client('s3')
    unique_name_with_timestamp = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + object_name
    
    print('Uploading data to S3:', unique_name_with_timestamp)

    # For JSON data, convert to string and encode to bytes
    if isinstance(data, dict):
        file_like_object = io.BytesIO(json.dumps(data).encode())
    else:
        # For plain text, just encode to bytes
        file_like_object = io.BytesIO(data.encode())

    # Upload the bytes to S3
    s3_client.upload_fileobj(file_like_object, bucket_name, unique_name_with_timestamp)
    
    print('Data uploaded successfully.')
