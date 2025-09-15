def print_kwargs(**kwargs):
    print("Keyword arguments received:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
        
print_kwargs(name= "Alice", age=30, city="New york", profession="Engineer")


  