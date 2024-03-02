# aurora-explorer-lambda-functions

This repository contains the AWS Lambda functions for the `Aurora Borealis Explorer` project. 

The primary function within this repository is designed to fetch, process, and store Aurora Borealis forecast data and the Hemispheric Power Index (HPI) data. 

Big thank you to `lambgeo/lambda-gdal` for adding a GDAL Lamda Layer. 

## Deployment

Make the script executable:
`chmod +x deploy.sh`

Then, to deploy the code (assuming you have write access to `s3://aurora-explorer-data/`), simply run:
`./deploy.sh`
