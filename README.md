# Excel Data Processor

A Python application for processing Excel sheets uploaded to an S3 bucket and storing data in DynamoDB using AWS CDK and Lambda.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Deployment](#deployment)
  - [Usage](#usage)

## Introduction

This application demonstrates how to create an AWS CDK stack that automates the process of processing Excel sheets uploaded to an S3 bucket and storing the parsed data in a DynamoDB table. The project uses AWS Lambda to perform the data processing when new Excel files are added to the S3 bucket.

## Features

- Automated processing of Excel sheets in an S3 bucket.
- Storage of parsed data in a DynamoDB table.
- Scalable and serverless architecture.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- AWS account with appropriate permissions.
- AWS CLI configured with your credentials.
- Python 3.8 or higher installed on your local machine.
- Node.js and npm installed (for AWS CDK).
- Git for version control.

## Getting Started

To get started with this project, follow these steps:

### Deployment

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Set up your AWS CDK environment:

   ```bash
   cd cdk-app
   npm install -g aws-cdk
   npm install

3. Deploy the AWS CDK Stack:

   ```bash
   cdk deploy

4. Deploy the Lambda Function:

    ```bash
    cd lambda
    pip install -r requirements.txt -t .

5. Run the deployment script:

    ```bash
   ./deploy_lambda.sh

## Usage

- Upload Excel sheets to the specified S3 bucket.
- The Lambda function will automatically process the Excel sheets and store the data in the DynamoDB table.
