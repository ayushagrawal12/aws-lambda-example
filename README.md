# AWS Lambda Example

This repository contains AWS Lambda functions for:
1. Adding two numbers via an API.
2. Uploading a file (PDF/Document) to an S3 bucket.

## Prerequisites
- Install [AWS CLI](https://aws.amazon.com/cli/)
- Install [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- Install Docker for local testing

## Project Structure

aws-lambda-example/
│
├── lambda_add_numbers/
│   ├── app.py            # Lambda function code for adding numbers
│   └── requirements.txt  # Any required dependencies (if any)
│
├── lambda_upload_file/
│   ├── app.py            # Lambda function code for uploading files to S3
│   └── requirements.txt  # Any required dependencies (if any)
│
└── template.yaml         # AWS SAM template file





