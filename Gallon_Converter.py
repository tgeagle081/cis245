# Miles to Kilometer conversion
# Author: Thomas Eagle
# Class: CIS245-T303
# Assignment: 6.1

# Define main function
def main():

  try:
    gallons_entered = int(input('Enter the Number of Gallons: '))

    Gallons_Converter(gallons_entered)

  except:
    print("An Error Occured, Please only enter a number")
    print()
    main()

def Gallons_Converter(gallons):
  liters = miles * 3.785
  print(gallons, 'gallons is equal to', liters, 'liters')

main()