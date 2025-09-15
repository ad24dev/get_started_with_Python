def event_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
        
print("Even numbers up to 10:")
for even in event_generator(10):
    print(even)
    
