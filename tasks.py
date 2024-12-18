import invoke


@invoke.task
def say_hello(_context):
    print("Hello, invoke command!")


@invoke.task
def say_hello_to_somebody(_context, name):
    print(f"Hello, {name}!")
