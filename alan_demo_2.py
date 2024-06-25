from prefect import task, flow
from prefect.deployments import run_deployment
from prefect.filesystems import S3
from prefect_aws import AwsCredentials


@flow
def input_number():
    number = int(input("Enter a number: "))
    return number

@flow
def addition_demo():
    number1 = run_deployment(name="input_number/input_number_xiangyuan", as_subflow=True)
    
