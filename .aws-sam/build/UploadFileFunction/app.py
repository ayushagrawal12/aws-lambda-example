import json
import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print("Event received:", event)
    
    try:
        body = json.loads(event.get('body', '{}'))
        print("Parsed body:", body)

        file_content = body.get('file_content')
        bucket_name = body.get('bucket_name')
        file_name = body.get('file_name')

        if not all([file_content, bucket_name, file_name]):
            raise ValueError("Missing required fields: file_content, bucket_name, or file_name")

        # Upload to S3
        response = s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content
        )
        print("File uploaded:", response)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully'})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
