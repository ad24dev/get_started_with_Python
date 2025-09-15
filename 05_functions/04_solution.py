import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2 
    circum = 2 * math.pi * radius
    return area, circum
  
area, circum = (calculate_circle_area(5))
print(f"Area is: {area:.2f}")
print(f"Circumference is: {circum:.2f}")




