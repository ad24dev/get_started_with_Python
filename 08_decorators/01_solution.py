import time

# Decorator that prints "Hello, world!" when the decorated function is called
# its a simple decorator example

# def decorator(func):
#     def wrapper():
#         return func()
#     return wrapper
  
  
# @decorator
# def hello():
#     print("Hello, world!")




def timer(func):
    def warapper(*args, **kwargs):
      start = time.time() 
      result = func(*args, **kwargs)
      end = time.time()
      print(f"Function {func.__name__} took {end - start} seconds to execute. ")
      
    
    return warapper
  
@timer  
def example_function(n):
      time.sleep(n)
      
example_function(2)


