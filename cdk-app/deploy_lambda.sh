#!/bin/bash

cd lambda
pip install -r requirements.txt -t .
cd ..

aws cloudformation package \
  --template-file cdk.out/template.yaml \
  --s3-bucket your-cdk-deployment-bucket \
  --output-template-file cdk.out/packaged-template.yaml

aws cloudformation deploy \
  --template-file cdk.out/packaged-template.yaml \
  --stack-name ExcelDataProcessorStack \
  --capabilities CAPABILITY_IAM
