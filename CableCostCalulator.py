# Cable Cost calculator
# Author: Thomas Eagle
# Class: CIS245-T303
# Assignment: 3.1

# print welcome message
print ("Welcome to Calculate the Fiber Optic Cable Price")

#Get Company Name for Order
CompanyName = input("Please enter the company name: ")

# Cost per foot of Cable
CostPerFeet = .87
CostPerFeet = float(CostPerFeet)

#Get Input for how many feet of cable they would like to order
FeetOfCable = input("How many feet of cable would you like to order? ")
FeetOfCable = float(FeetOfCable)

#Calculate cost of cable multiplying the Feet of Cable by the Cost per foot
Cost = FeetOfCable * CostPerFeet

#Create message for the cost of the total cable for the company 
message  = "The cost for " + CompanyName + " is: " + str(Cost)

#Display Message
print(message)