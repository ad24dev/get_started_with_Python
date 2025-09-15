score = input("Enter your score: ")

score = int(score)

if score > 100 or score < 0:
    print("Invalid Score")
    exit()

if score >= 90:
    print("A");
elif score >= 80:
    print("B")
elif score >= 70:  
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
    
    