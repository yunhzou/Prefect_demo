from prefect import flow, deploy 



if __name__ == "__main__":
    # flow.from_source(
    #     source="https://github.com/prefecthq/demos.git",
    #     entrypoint="my_gh_workflow.py:repo_info",
    # ).deploy(
    #     name="my-first-deployment",
    #     work_pool_name="Test-WorkPool",
    # )

    # source = "https://github.com/yunhzou/Prefect_demo.git"
    # entrypoint = "create_flowrun.py:test_flow"
    # flow.from_source(source=source, entrypoint=entrypoint).deploy(name="test_flow_run", work_pool_name="Test_WorkPool")

    source = "https://github.com/yunhzou/Prefect_demo.git"
    entrypoint = "prefect_demo.py:add_numbers"
    #flow.from_source(source=source, entrypoint=entrypoint).deploy(name="show_text_image_xiangyuan", work_pool_name="Test_WorkPool")
    flow.from_source(source=source, entrypoint=entrypoint).deploy(name="add_numbers", work_pool_name="Jackie Computer")