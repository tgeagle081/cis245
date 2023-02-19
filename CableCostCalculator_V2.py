# Cable Cost calculator
# Author: Thomas Eagle
# Class: CIS245-T303
# Assignment: 4.1

# print welcome message
print ("Welcome to Calculate the Fiber Optic Cable Price")

#Get Company Name for Order
CompanyName = input("Please enter the company name: ")

#Get Input for how many feet of cable they would like to order
FeetOfCable = input("How many feet of cable would you like to order? ")
FeetOfCable = float(FeetOfCable)

# Determine cost of foot per cable by amount of feet ordered

if FeetOfCable > 500:
  CostPerFeet = .50
elif FeetOfCable > 250:
  CostPerFeet = .70
elif FeetOfCable > 100:
  CostPerFeet = .80
else:
  CostPerFeet = .87

CostPerFeet = float(CostPerFeet)

#Calculate cost of cable multiplying the Feet of Cable by the Cost per foot
Cost = FeetOfCable * CostPerFeet

#Create message for the cost of the total cable for the company 
message  = "The cost for " + CompanyName + " is: " + str(Cost)

#Display Message
print(message)