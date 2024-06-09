from prefect import task, flow

@flow
def add(a):
    return a + 1

@flow(log_prints=True)
def my_flow():
    num = 1
    while num < 10:
        num = add(num)
        print(num)


@task
def add_t(a):
    return a + 1

@flow(log_prints=True)
def my_flow_t():
    num = 1
    while num < 10:
        num = add_t(num)
        print(num)

if __name__ == "__main__":
    my_flow()
    #my_flow_t()