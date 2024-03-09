#!/bin/bash

echo "Installing dependencies..."
mkdir python
pip install -r requirements.txt -t python/

echo "Copying Python files to the package directory..."
cp *.py python/

echo "Creating the deployment package..."
cd python || exit
zip -r9 ../k8-job-trigger.zip .
cd .. || exit

rm -rf python

echo "Copying to S3 Storage..."
aws s3 cp k8-job-trigger.zip s3://aurora-explorer-data/

echo "k8-job-trigger.zip package has been uploaded to S3."
echo "Please run Terraform to update the AWS Lambda function."
