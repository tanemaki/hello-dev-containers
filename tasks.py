import invoke


@invoke.task
def say_hello(_context):
    print("Hello, invoke command!")


@invoke.task
def say_hello_to_somebody(_context, name):
    print(f"Hello, {name}!")


@invoke.task
def say_hello_using_private_library(_context):
    # This is a private library defined under src/hello_dev_containers
    import hello_dev_containers

    print(hello_dev_containers.hello())
