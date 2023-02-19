# Miles to Kilometer conversion
# Author: Thomas Eagle
# Class: CIS245-T303
# Assignment: 6.1

# Define main function
def main():

  try:
    # get the number of miles driven
    miles_entered = int(input('Enter the Number of Miles driven: '))

    # Miles Converter function called
    Miles_Converter(miles_entered)

  except:
    # if the entered item is not an integer, display this error message and recall the main function
    print("An Error Occured, Please only enter a number")
    print()
    main()

#Define Miles_Converter function that converts the miles entered to kilometers
def Miles_Converter(miles):
  kilometers = miles * 1.609344
  print(miles, 'Miles is equal to', kilometers, 'Kilometers driven')

# Call the Main function
main()