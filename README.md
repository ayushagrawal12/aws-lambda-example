# AWS Lambda Project

This project contains AWS Lambda functions for:
1. Adding two numbers (`lambda_add_numbers`)
2. Uploading a document to an S3 bucket (`lambda_upload_file`)

These functions are deployed using AWS SAM (Serverless Application Model) and can also be tested locally.

## Prerequisites
Before running the project, ensure you have the following installed:
- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [Docker](https://www.docker.com/get-started) (Required for local execution)
- Python 3.10 or later

## Project Structure
```
aws-lambda-example/
│── lambda_add_numbers/
│   ├── app.py  # Lambda function for addition
│   ├── requirements.txt  # Dependencies
│── lambda_upload_file/
│   ├── app.py  # Lambda function for file upload
│   ├── requirements.txt  # Dependencies
│── template.yaml  # AWS SAM template
│── README.md  # Documentation
```

## Setup and Running Locally

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/aws-lambda-example.git
cd aws-lambda-example
```

### 2. Install Dependencies
```sh
pip install -r lambda_add_numbers/requirements.txt -t lambda_add_numbers/
pip install -r lambda_upload_file/requirements.txt -t lambda_upload_file/
```

### 3. Start the API Locally
```sh
sam build
sam local start-api
```

### 4. Test the API Endpoints
#### Test Addition Function
```sh
Invoke-WebRequest -Uri http://127.0.0.1:3000/add -Method POST -Body '{"num1": 5, "num2": 10}' -ContentType 'application/json'

```
Expected Response:
```json
Content : {"result": 15}
```

#### Test File Upload Function
```sh
Invoke-WebRequest -Uri http://127.0.0.1:3000/upload -Method POST -Body '{"file_content": "This is a test file content", "bucket_name": "your-s3-bucket-name", "file_name": "test.txt"}' -ContentType 'application/json'

```
Expected Response:
```json
{
    "message": "File uploaded successfully"
}
```

## Deploy to AWS
To deploy the Lambda functions to AWS:
```sh
sam build
sam deploy --guided
```
Follow the prompts to configure the deployment.

## Cleanup
To remove deployed resources from AWS:
```sh
sam delete
```
