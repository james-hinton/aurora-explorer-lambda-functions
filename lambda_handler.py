import boto3
from data_retrieval import fetch_aurora_data, fetch_hpi_data
from data_processing import process_aurora_data, process_hpi_data
from storage import store_in_dynamodb, store_in_s3
from geospatial_conversion import generate_geotiff


def lambda_handler(event, context):
    aurora_data = fetch_aurora_data()
    hpi_data = fetch_hpi_data()

    # Process the data
    processed_aurora_data = process_aurora_data(aurora_data)
    processed_hpi_data = process_hpi_data(hpi_data)

    # Store data in DynamoDB and S3 (pseudo-code)
    store_in_dynamodb(processed_aurora_data, processed_hpi_data)
    geo_tiff = generate_geotiff(processed_aurora_data)
    store_in_s3(geo_tiff, "aurora-explorer-data")

    return {
        "statusCode": 200,
        "body": "Data processing and storage completed successfully.",
    }


if __name__ == "__main__":
    lambda_handler(None, None)
