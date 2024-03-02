#!/bin/bash

echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt
pip install -r requirements.txt -t ./package/

echo "Copying Python files to the package directory..."
cp *.py ./package/

echo "Creating the deployment package..."
cd package || exit
zip -r9 ../package.zip .
cd .. || exit

echo "Copying to S3 Storage..."
aws s3 cp package.zip s3://aurora-explorer-data/

echo "Deployment package has been uploaded to S3."
echo "Please run Terraform to update the AWS Lambda function."
