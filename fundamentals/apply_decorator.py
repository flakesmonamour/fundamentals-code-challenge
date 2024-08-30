def decorator_function(func):
    def wrapper():
        print("This is a decorator function")
        return func()
    return wrapper

def apply_decorator(func):
    return decorator_function(func)

def say_hello():
    print("Hello, New generation!")

decorator_function=apply_decorator(say_hello)

decorator_function()