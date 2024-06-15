from huey.contrib.djhuey import task

@task()
def count():
    for i in range(10):
        print(i)