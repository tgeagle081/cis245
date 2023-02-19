# Investment calculator
# Author: Thomas Eagle
# Class: CIS245-T303
# Assignment: 5.1

#print Welcome Message
print("Welcome to Investment Calculator")

#Get the amount of money for the intial investment
InvestAmount = input("Enter The Initial Investment Amount: ")
InvestAmount = float(InvestAmount)

#Get The Interest Rate the Investment will be growing at
InterestRateRaw = input("Enter Annual Interest Rate: ")
InterestRateRaw = float(InterestRateRaw)

#convert the interest rate into a percentage
InterestRate = InterestRateRaw / 100

#Initiate the Year variable 
Year = 1

#get the goal of doubling the investment amount
GoalAmount = InvestAmount * 2
GoalAmount = float(GoalAmount)

#Determine how long it takes to double the investment
while(InvestAmount < GoalAmount):
  #Get the Amount of Growth for the year from the investment amount times the Interest Rate
  InterestAmount = InvestAmount * InterestRate
  #get the total amount of the Investment Amount plus the amount of growth over the year 
  InvestAmount = InvestAmount + InterestAmount
  #Displace Message of of year and the total amount of the investment rounded to 2 decimal places. 
  Message = "Year " + str(Year) + " Investment Amount is $" + '%.2f' %InvestAmount
  print(Message)
  #Add to the year to show the years it takes.
  Year = Year + 1

#Display exit message
print ("Thanks for using the investment Calculator!")