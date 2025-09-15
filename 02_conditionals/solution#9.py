# Recommend a type of pet food based on the pet's secies and age. (e.g, Dog: < 2 yeas - Puppy food, Cat: > 5 years - Senior cat food.)
species = "Dog"
age = 3

if species == "Dog":
    if age < 2:
        print("Puppy food")
    elif 2 <= age <= 7:
        print("Adult dog food")
    else:
        print("Senior dog food")
elif species == "Cat":
    if age < 2:
        print("Kitten food")
    elif 2 <= age <= 10:
        print("Adult cat food")
    else:
        print("Senior cat food")
        
        