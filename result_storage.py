from prefect import flow, task

@flow(log_prints=True)
def my_flow():
    a = hello_world()
    print(a)


@task(persist_result=True, result_storage_key="{flow_run.flow_name}_{flow_run.name}_hello.json")
def hello_world(name: str = "world"):
    return f"hello {name}"

my_flow()