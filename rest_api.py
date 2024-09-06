import asyncio
from prefect.client import get_client
from prefect.client.orchestration import get_client

async def get_flows():
    client = get_client()
    r = await client.read_flows(limit=20)
    return r

async def get_deployments():
    client = get_client()
    r = await client.read_deployments(limit = 20)
    return r

r = asyncio.run(get_deployments())

for flow in r:
    #print(type(flow))
    #print(dict(flow))
    print(flow.name, flow.id, flow.description, flow.parameter_openapi_schema)
    #print(flow)
    print()