from prefect import flow
from prefect.deployments import run_deployment


@flow
def print_remote_control():
    # Emoji for remote control
    print(1)



def demo(): 
    run_deployment(name="print_remote_control/print_remote_control_virtual", as_subflow=True)
    run_deployment(name="print_remote_control/print_remote_control_local", as_subflow=True)

if __name__ == "__main__":
    source = "https://github.com/yunhzou/Prefect_demo.git"
    entrypoint = "alan_demo.py:print_remote_control"
    flow.from_source(source=source, entrypoint=entrypoint).deploy(name="print_remote_control_local", work_pool_name="Jackie Computer")
    flow.from_source(source=source, entrypoint=entrypoint).deploy(name="print_remote_control_virtual", work_pool_name="Test_WorkPool")
    #demo()