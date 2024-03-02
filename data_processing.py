import json

def process_aurora_data(event, context):
    # Process the data
    return {"statusCode": 200, "body": json.dumps("Data processed successfully")}


def process_hpi_data(event, context):
    # Process the data
    return {"statusCode": 200, "body": json.dumps("Data processed successfully")}
