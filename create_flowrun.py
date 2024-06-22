import asyncio
from prefect import get_client
from prefect.flow_runs import wait_for_flow_run
from prefect import flow, deploy
from prefect.deployments import run_deployment
from prefect.filesystems import S3
from prefect_aws.s3 import S3Bucket
from prefect_aws import AwsCredentials


@flow 
async def main():
    async with get_client() as client:
        flow_run = await client.create_flow_run_from_deployment(deployment_id="b06a9db9-df44-4029-a97b-4cb86b7a2637")
        flow_run = await wait_for_flow_run(flow_run_id=flow_run.id)
        #flow_run_1 = await client.create_flow_run_from_deployment(deployment_id="b06a9db9-df44-4029-a97b-4cb86b7a2637")
        #flow_run_1 = await wait_for_flow_run(flow_run_id=flow_run.id)
        print(flow_run.state)
        #print(flow_run_1.state)

class test_object:
    def __init__(self, name):
        self.name = name

    def run(self):
        return f"Hello {self.name}!"


#s3_bucket_block = S3Bucket.load("jackie-bucket")
aws_credentials = AwsCredentials.load("jackie-aws-credentials")
s3bucket = S3(bucket_path="testbucketjackie/result_storage", credentials=aws_credentials)


#test flow run with actual parameters
@flow(persist_result=True,result_storage=s3bucket)
def test_flow(name):
    return test_object(name)

@flow(log_prints=True)
def run_deployment_test():
    parameter = {"name": "world"}
    flow_run = run_deployment(name="f3f46e0e-7f85-4d8f-a0f8-db07a2accbd4",as_subflow=True, parameters=parameter)
    print(flow_run.state.result().run())
#Note run_deployment is also a valid method to create a flow run. 
if __name__ == "__main__":
    #deploy
    #asyncio.run(main())
    run_deployment_test()
