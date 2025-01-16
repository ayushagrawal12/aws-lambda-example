import json

def lambda_handler(event, context):
    print("Event received:", event)  # Log the full event
    
    try:
        # Parse the body from the event
        body = json.loads(event.get('body', '{}'))
        print("Parsed body:", body)  # Log the parsed body

        # Extract numbers
        num1 = body.get('num1')
        num2 = body.get('num2')

        print("num1:", num1, "num2:", num2)  # Log the extracted values

        # Validate inputs
        if num1 is None or num2 is None:
            raise ValueError("num1 and num2 are required fields.")

        # Ensure numbers are integers
        result = int(num1) + int(num2)
        print("Result:", result)  # Log the result

        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except (ValueError, json.JSONDecodeError) as e:
        print("Error:", str(e))  # Log the error
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
