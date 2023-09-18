from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_dynamodb as dynamodb,
    aws_iam as iam,
    core,
)

class ExcelDataProcessorStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket
        data_bucket = s3.Bucket(
            self, "DataBucket",
            removal_policy=core.RemovalPolicy.DESTROY,
        )

        # Create a DynamoDB table
        data_table = dynamodb.Table(
            self, "DataTable",
            partition_key={"name": "ID", "type": dynamodb.AttributeType.STRING},
            removal_policy=core.RemovalPolicy.DESTROY,
        )

        # Create an IAM role for the Lambda function
        lambda_role = iam.Role(
            self, "LambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        # Grant S3 read permissions to the Lambda function
        data_bucket.grant_read(lambda_role)

        # Grant DynamoDB write permissions to the Lambda function
        data_table.grant_write_data(lambda_role)

        # Create the Lambda function
        excel_processing_lambda = _lambda.Function(
            self, "ExcelProcessingLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.handler",
            code=_lambda.Code.from_asset("lambda"),  # Create a 'lambda' directory with your Lambda code.
            role=lambda_role,
            environment={
                "DYNAMODB_TABLE_NAME": data_table.table_name,
            },
        )

        # Add an S3 event trigger to the Lambda
        s3_event_trigger = events.Rule(
            self, "S3EventRule",
            event_pattern={
                "source": ["aws.s3"],
                "eventName": ["ObjectCreated:*"],
                "eventSource": [{"prefix": data_bucket.bucket_name}],
            },
        )
        s3_event_trigger.add_target(targets.LambdaFunction(excel_processing_lambda))
