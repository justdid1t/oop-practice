class Car:
    
    def __init__(self,brand,year,country):
        self.brand = brand
        self.year = year
        self.country = country
        
    def display_info(self):
        return f'''

brand = {self.brand}
year = {self.year}
country = {self.country}

'''
        
        

toyota  = Car('Toyota',2024,'Japan')  #object1
tesla = Car('Tesla',2025,'US')   #object2

#print(toyota.display_info())
print(tesla.display_info())
        
        
    