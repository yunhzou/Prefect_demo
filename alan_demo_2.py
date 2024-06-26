from prefect import task, flow
from prefect.deployments import run_deployment
from prefect.filesystems import S3
from prefect_aws import AwsCredentials


@flow(persist_result=True, 
      result_storage=S3(bucket_path="testbucketjackie/result_storage", 
                        credentials=AwsCredentials.load("jackie-aws-credentials")))
def input_number():
    number = int(input("Enter a number: "))
    return number

@flow(log_prints=True,)
def add_numbers():
    local_num = run_deployment(name="input-number/input_number_local", as_subflow=True)
    num1 = local_num.state.result()
    print(f"Local number: {num1}")
    virtual_num = run_deployment(name="input-number/input_number_virtual", as_subflow=True)
    num2 = virtual_num.state.result()
    print(f"Virtual number: {num2}")
    sum = num1 + num2
    print(f"Sum: {sum}")

if __name__ == "__main__":
    # source = "https://github.com/yunhzou/Prefect_demo.git"
    # entrypoint = "alan_demo_2.py:input_number"  
    # flow.from_source(source=source, entrypoint=entrypoint).deploy(name="input_number_local", work_pool_name="Jackie Computer")
    # flow.from_source(source=source, entrypoint=entrypoint).deploy(name="input_number_virtual", work_pool_name="Test_WorkPool")
    add_numbers()