from prefect import task, flow,get_client
from prefect.deployments import run_deployment
from prefect.filesystems import S3
from prefect_aws import AwsCredentials
import tkinter as tk
from tkinter import simpledialog
import asyncio


@flow(persist_result=True, 
      result_storage=S3(bucket_path="testbucketjackie/result_storage", 
                        credentials=AwsCredentials.load("jackie-aws-credentials")))
def input_number():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    number = simpledialog.askinteger("Input", "Enter a number:")
    root.destroy()  # Destroy the main window after getting the input
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


@flow(log_prints=True)
async def add_numbers_async():
    async def get_number(name):
        deployment = await run_deployment(name=name, as_subflow=True)
        num = await deployment.state.result().get()
        return num

    local_num_future = get_number("input-number/input_number_local")
    virtual_num_future = get_number("input-number/input_number_virtual")
    num1, num2 = await asyncio.gather(local_num_future, virtual_num_future)
    print(f"Local number: {num1}")
    print(f"Virtual number: {num2}")
    sum = num1 + num2
    print(f"Sum: {sum}")

if __name__ == "__main__":
    #asyncio.run(add_numbers_async())
    #To Deploy run the code below
    #source = "https://github.com/yunhzou/Prefect_demo.git"
    #entrypoint = "demo.py:input_number"  
    #flow.from_source(source=source, entrypoint=entrypoint).deploy(name="input_number_local", work_pool_name="Jackie Computer")
    #flow.from_source(source=source, entrypoint=entrypoint).deploy(name="input_number_virtual", work_pool_name="Test_WorkPool")
    add_numbers()