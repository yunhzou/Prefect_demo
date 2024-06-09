import asyncio
from prefect import get_client
from prefect.flow_runs import wait_for_flow_run
from prefect import flow, deploy
from prefect.deployments import run_deployment

@flow 
async def main():
    async with get_client() as client:
        flow_run = await client.create_flow_run_from_deployment(deployment_id="b06a9db9-df44-4029-a97b-4cb86b7a2637")
        flow_run = await wait_for_flow_run(flow_run_id=flow_run.id)
        #flow_run_1 = await client.create_flow_run_from_deployment(deployment_id="b06a9db9-df44-4029-a97b-4cb86b7a2637")
        #flow_run_1 = await wait_for_flow_run(flow_run_id=flow_run.id)
        print(flow_run.state)
        #print(flow_run_1.state)



#test flow run with actual parameters
@flow(persist_result=True)
def test_flow(name):
    return f"Hello {name}!"

@flow(log_prints=True)
def run_deployment_test():
    parameter = {"name": "world"}
    flow_run = run_deployment(name="66dc6697-b030-453d-9418-d7a6e3b1a00d",as_subflow=True, parameters=parameter)
    print(flow_run.state.result().get())

     
#Note run_deployment is also a valid method to create a flow run. 
if __name__ == "__main__":
    #deploy
    #asyncio.run(main())
    run_deployment_test()
