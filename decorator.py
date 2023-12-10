def my_decorator(function):
    def wrapper():
        print('Header')
        function()
        print('Footer')
    return wrapper

@my_decorator
def standalone_function():
    print('Standalone')

standalone_function()