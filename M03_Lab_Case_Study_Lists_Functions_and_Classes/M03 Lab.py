""" 
Tyler Joerendt
M03 Lab.py
This program will take a vehicle type and collect all of its attributes and then display them. 

Variables:

year, make, model, doors, roof - All of these are the different attributes that are collecrted in the input for a car 

vehi_type- is what decides what vehicle is being inputed currently the code is only made for a car however can be expanded for much more vehicles

class vehicle- is the parent class that takes all of the attributes for each vehicle type and associates it with the vehicle like for a car we get 
year, make, model, doors, roof

class automobile- is a class that associates all the attributes to a car
"""

class vehicle:
    def __init__(self,vehi_type):
        self.vehi_type = vehi_type
class automobile(vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__('car')
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def info(self):
        print("________________________")
        print(f"Vehicle Type: {self.vehi_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number Of Doors: {self.doors}")
        print(f"Type of Roof: {self.roof}")
        print("________________________")
        """ At first I didn't put this in the class and I couldn't get the self.attributes to work but then I realized I needed them 
        in the class itself to work properly """

self = str(input("What is your name? ").upper())

vehi_type = str(input("What type of vehicle do you have? ").upper())
if vehi_type == 'CAR':

    year = int(input("What year was your car made? "))

    make = str(input("What is your car's make? ").upper())

    model = str(input("What is your car's model? ").upper())

    doors = int(input("How many doors does your car have 2 or 4? "))
    while doors != 2 and doors != 4:
        print("invalid option please choose 2 or 4 ")
        doors = int(input("How many doors does your car have 2 or 4? "))

    roof = str(input("Is your roof solid or a sun roof? ").upper())
    while roof != 'SOLID' and roof != 'SUN ROOF':
        print("Invalid option please choose solid or sun roof")
        roof = str(input("Is your roof solid or a sun roof? "))
    
    car = automobile(year, make, model, doors, roof)
    car.info()

else:
    print("Sorry we don't have that vehicle yet added for attribute description")

    