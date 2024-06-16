from prefect_aws import AwsCredentials

# aws_credentials_block = AwsCredentials.load("aws-jackie")

# print(aws_credentials_block)


from prefect_aws.s3 import S3Bucket

s3_bucket_block = S3Bucket.load("jackie-bucket")