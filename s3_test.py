from pathlib import Path
from prefect import flow
from prefect_aws import AwsCredentials, S3Bucket


@flow(persist_result=True)
def s3_flow():
    # create a dummy file to upload
    file_path = Path("test-example.txt")
    file_path.write_text("Hello, Prefect!")

    aws_credentials = AwsCredentials.load("jackiecre")
    # s3_bucket = S3Bucket(
    #     bucket_name="testbucketjackie",
    #     credentials=aws_credentials
    # )
    s3_bucket=S3Bucket.load("s3")

    s3_bucket_path = s3_bucket.upload_from_path(file_path)
    downloaded_file_path = s3_bucket.download_object_to_path( "downloaded-test-example.txt"
    )
    return downloaded_file_path.read_text()


if __name__ == "__main__":
    s3_flow()
