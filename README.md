# Aurora Explorer Lambda Functions
For project details, see the [project gist](https://gist.github.com/james-hinton/153704719a4546f78cb6dd2fe545d4c6).

This repository contains AWS Lambda functions developed for the Aurora Explorer project. These functions facilitate data retrieval from external sources and trigger Kubernetes jobs for data processing.

## Functions

- **retrieve_data**: Fetches Aurora Borealis forecast data from NOAA's API and stores it in AWS S3.
- **k8_job_trigger**: Triggers a Kubernetes job for processing the retrieved Aurora data.

## Deployment

Each function directory includes a `deploy.sh` script for deploying the Lambda function to AWS.

For more information on the functionality and deployment process of each Lambda function, refer to the README.md within the respective function directory.
