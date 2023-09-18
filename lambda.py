import os
import json
import boto3
from io import BytesIO
import pandas as pd

# Retrieve environment variables
DYNAMODB_TABLE_NAME = os.environ.get("DYNAMODB_TABLE_NAME")

# Create a DynamoDB client
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

def lambda_handler(event, context):
    for record in event["Records"]:
        # Extract S3 bucket and object information
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        # Download the Excel file from S3
        s3_client = boto3.client("s3")
        response = s3_client.get_object(Bucket=bucket, Key=key)
        excel_data = response["Body"].read()

        # Parse the Excel data using Pandas
        df = pd.read_excel(BytesIO(excel_data))

        # Convert the DataFrame to a list of dictionaries
        data_to_insert = df.to_dict(orient="records")

        # Insert data into DynamoDB
        for item in data_to_insert:
            table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps("Data inserted into DynamoDB successfully."),
    }
