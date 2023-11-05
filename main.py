from prefect import flow, task

@task
def master_task():
    msg = "This is the task"
    return(msg) 

@flow
def sub_flow():
    msg = "This is the sub flow"
    return(msg)


@flow
def master_flow():
    sub_flow_msg = sub_flow()
    task_msg = master_task()
    all_msg = sub_flow_msg + task_msg
    print(all_msg)

if __name__ == "__main__":
    master_flow()