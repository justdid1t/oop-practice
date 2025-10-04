class Car:  #class declaration
    
    brand = 'Toyota'   #attributes
    model = 'roadstar'
    year = 2025
    mileage = '40 km/L'
    
    
    def start(self):    #methods
        return f'{self.brand} is now runing ....'
    
    def stop(self):
        return 'car has stopped!'
    
    def display_info(self):
        return f'''
 brand = {self.brand}
  model = {self.model}
   year = {self.model}
    mileage = {self.mileage}
                   
                 '''
    
my_car = Car()  #object

# print(my_car.brand)
# print(my_car.mileage)
# print(my_car.model)

print(my_car.display_info())
    
    