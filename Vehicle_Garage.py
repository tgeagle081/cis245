# Stocker Ticker Lookup
# Author: Thomas Eagle
# Class: CIS245-T303
# Assignment: 8.1

# Define Vehicle Class
class vehicle:
  #set Vehicle Make Method
  def setVehicleMake(self, make):
    self.vehicle_make = make

  #set Vehicle Model Method
  def setVehicleModel(self, model):
    self.vehicle_model = model

  #display Vehicle Make Method
  def getVehicleMake(self):
    print(f"The Make of the vehicle is: {self.vehicle_make}")

  #display Vehicle Model Method
  def getVehicleModel(self):
    print(f"The Model of the vehicle is: {self.vehicle_model}")

#define car class with inheritence from Vehicle Class
class car(vehicle):
  #set number of car doors method
  def setCarDoor(self, door):
    self.car_door = door

  #display number of car doors method
  def getCarDoor(self):
    print(f"The Number of Car Doors is: {self.car_door}")

#define pickup class with inheritence from Vehicle Class
class pickup(vehicle):
  #set length of truck bed method
  def setBedLength(self, bed):
    self.truck_bed = bed

  #display length of truck bed
  def getBedLength(self):
    print(f"The Length of the Truck Bed is: {self.truck_bed}")

# Function to display when a vehicle has been entered into the garage
def Entered_Message():
  print("Vehicle has been added to the Virtual Garage")
  print("")

# Function for Car Entry
def enter_car():
  input_make = input("Please enter the Make of the Car: ")
  input_model = input("please enter the Model of the Car: ")
  input_door = input("Please enter the number of Doors on the Car: ")
  print("")
  new_car = car()
  new_car.setVehicleMake(input_make)
  new_car.setVehicleModel(input_model)
  new_car.setCarDoor(input_door)
  new_car.getCarDoor()
  new_car.getVehicleMake()
  new_car.getVehicleModel()
  Entered_Message()

#Function for Pickup Entry  
def enter_truck():
  input_make = input("Please enter the Make of the Truck: ")
  input_model = input("please enter the Model of the Truck: ")
  input_bed = input("Please enter the Length of the Truck Bed: ")
  print("")
  new_truck = pickup()
  new_truck.setVehicleMake(input_make)
  new_truck.setVehicleModel(input_model)
  new_truck.setBedLength(input_bed)
  new_truck.getBedLength()
  new_truck.getVehicleMake()
  new_truck.getVehicleModel()
  Entered_Message()

#welcome Message
print("Welcome to the Virtual Vehicle Garage")
print("")

#intiate variable used in while loop
choice = 0

#while loop to allow continous entry
while choice != 3:
  print("1 to Enter a Car")
  print("2 to Enter a truck")
  print("3 to quit program")
  try:
    choice = int(input("Enter your Option: "))

  #capture error for when a non-integer is entered
  except:
    print("Please enter a valid number, 1, 2, or 3")

  #if Integer is entered, evaluate it for Car, Truck, or quit
  else:
    if choice == 1:
      enter_car()
    elif choice == 2:
      enter_truck()
    elif choice != 3:
      # It 1, 2, or 3 is not entered, display message and start loop again
      print("Please enter a valid number, 1, 2, or 3")