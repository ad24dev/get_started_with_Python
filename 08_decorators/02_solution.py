


def debug (func):
    def wrapper(*agrs, **kwargs):
        args_value = ', '.join(str(arg) for arg in agrs)
        kwargs_value = ', '.join(f"{key}= {value}" for key, value in kwargs.items())
        print(f"Function {func.__name__} called with arguments: {args_value}, {kwargs_value}") 
        return func(*agrs, **kwargs)
     
    return wrapper



@debug
def greeting(name, greet="Hello"):
    return f"{greet}, {name}!"
  
print(greeting("Alice"))