def sum_all(*args):
    print("Arguments received:", args)
    for i in args:
        print(i)
    return sum(args)
  
  
print("Sum is:", sum_all(1, 2, 3, 4, 5))
