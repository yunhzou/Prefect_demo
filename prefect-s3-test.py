from prefect import flow
from prefect_aws.s3 import S3Bucket
from prefect.filesystems import LocalFileSystem, S3
from prefect_aws import AwsCredentials

@flow(persist_result=True)
def test_flow():
    return "Hello, world!"


if __name__ == "__main__":
    aws_credentials = AwsCredentials.load("jackie-aws-credentials")
    s3bucket = S3(bucket_path="testbucketjackie/result_storage", credentials=aws_credentials)
    new_flow = test_flow.with_options(result_storage=s3bucket)
    new_flow()