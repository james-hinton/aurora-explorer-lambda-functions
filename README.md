# aurora-explorer-lambda-functions

This repository contains the AWS Lambda functions for the `Aurora Borealis Explorer` project. 

The primary function within this repository is designed to fetch, process, and store Aurora Borealis forecast data and the Hemispheric Power Index (HPI) data. 

Big thank you to `lambgeo/lambda-gdal` for adding a GDAL Lamda Layer. 

How to redeploy this code:

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`pip install -r requirements.txt -t ./package/`

`cp *.py ./package/`

`cd package`

`zip -r9 ../package.zip .`

`cd ..`

Copy to S3 Storage
`aws s3 cp package.zip s3://aurora-explorer-data/`

And then Terraform will pick up the change