from data_retrieval import fetch_aurora_data, fetch_hpi_data
from storage import store_in_s3


def lambda_handler(event, context):
    aurora_data = fetch_aurora_data()
    hpi_data = fetch_hpi_data()

    store_in_s3(
        aurora_data,
        "aurora-explorer-data",
        "aurora-data-raw",
        "aurora-data-gridded.json",
    )
    store_in_s3(
        hpi_data, "aurora-explorer-data", "aurora-hemi-raw", "aurora-hemi-power.txt"
    )

    return {"statusCode": 200, "body": "Data retrieved and stored in S3."}


if __name__ == "__main__":
    lambda_handler(None, None)
