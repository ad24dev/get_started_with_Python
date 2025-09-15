age = 10
day = "Wednesday"

#if age >= 18 and day == "Wednesday":
 #   print("you will get the ticket on $12") 
#elif age >= 18:
 #      print("you will get the ticket on $10")
#elif age < 18 and day == "Wednesday":
  #  print("you will get the ticket on $8")
##   print("you will get the ticket on $6")
    
    
price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2
    
print(f"you will get the ticket on ${price}")
