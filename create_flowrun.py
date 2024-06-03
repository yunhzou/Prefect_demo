import asyncio
from prefect import get_client
from prefect.flow_runs import wait_for_flow_run
from prefect import flow

@flow 
async def main():
    async with get_client() as client:
        flow_run = await client.create_flow_run_from_deployment(deployment_id="b06a9db9-df44-4029-a97b-4cb86b7a2637")
        flow_run = await wait_for_flow_run(flow_run_id=flow_run.id)
        flow_run_1 = await client.create_flow_run_from_deployment(deployment_id="b06a9db9-df44-4029-a97b-4cb86b7a2637")
        flow_run_1 = await wait_for_flow_run(flow_run_id=flow_run.id)
        print(flow_run.state)
        print(flow_run_1.state)



#test flow run with actual parameters
@flow
def test_flow(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    #deploy
    test_flow.serve(name="test-flow")