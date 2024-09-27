from prefect import flow, task,serve
from prefect.futures import wait
from prefect.task_runners import ThreadPoolTaskRunner
import time
import asyncio
from prefect.deployments import run_deployment




@task
def stop_at_floor(floor):
    print(f"elevator moving to floor {floor}")
    time.sleep(floor)
    print(f"elevator stops on floor {floor}")


@flow(task_runner=ThreadPoolTaskRunner(max_workers=5))
def elevator():
    floors = []

    for floor in range(10, 0, -1):
        floors.append(stop_at_floor.submit(floor))

    wait(floors)


@flow(log_prints=True, persist_result=True)
def stop_at_floor_flow(floor):
    print(f"elevator moving to floor {floor}")
    time.sleep(floor)
    print(f"elevator stops on floor {floor}")
    return floor


@flow
async def d_elevator():
    tasks = [run_deployment(name="stop-at-floor-flow/stop_at_floor",
                            parameters={'floor':i},) for i in range(10, 0, -1)]
    result = await asyncio.gather(*tasks)
    return result



if __name__ == "__main__":
    deployed_floor = stop_at_floor_flow.to_deployment(name="stop_at_floor")
    serve(deployed_floor)
