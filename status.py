def lambda_handler(event, context):
    print("Hello, World!")
    return {
        'statusCode': 200,
        'body': 'Status okay, Aurora Explorer lambda function is running!'
    }
