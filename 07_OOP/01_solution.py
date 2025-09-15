class Car:
  
    total_cars = 0
  
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1
    
    def full_name(self):
        return f"{self.brand} {self.__model}"
      
    def get_brand(self):
        return self.__brand + " !"
    
   
    # tell about this method fuell_type
    # this method is meant to be overridden in subclasses
    # it provides a default implementation for the base class
    # subclasses can provide their own implementation
    # this is an example of polymorphism
    # polymorphism allows methods to do different things based on the object calling them
    # it allows for flexibility and extensibility in code  
    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    # static method does not depend on instance or class variables
    # it is a utility function related to the class
    # we use it when we want to group a function with a class but it doesn't need access to instance or class data
    def general_description():
        return "Cars are vehicles with four wheels."
    
    @property
    # write cooment about @property why we usse it 
    # it is used to make a method behave like an attribute
    # it allows us to access the method without parentheses
    def model(self):
        return self.__model
    
      

class ElectricCar(Car):
  
    def __init__(self, brand, model, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(brand, model)
        
    # overriding the fuel_type method from the base class
    # this is an example of method overriding
    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "100 kWh")

# isinstance (my_tesla, ElectricCar) 
# print(isinstance (my_tesla, Car))




# print(my_tesla.brand)
# print(my_tesla.get_brand())

# print(my_tesla.fuel_type())

# safari = Car("Land Rover", "Defender")
# safari.model = "City" 
# print(safari.model)



# print(safari.general_description())


# my_car =  Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())  

# my_new_car = Car("Honda", "Civic")
# print(my_new_car.brand)
# print(my_new_car.model)


class battery_info:
   def battery_info(self):
    return ("This is battery info method")
  

class EngineInfo: 
    def engine_info(self):
      return ("This is engine info method")
  
class ElectricCarTwo(battery_info, EngineInfo, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model")
 
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())

