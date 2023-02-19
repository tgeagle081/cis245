# Address Book
# Author: Thomas Eagle
# Class: CIS245-T303
# Assignment 10.1 

# Define the build_input function to build the input string that will be added to the line
def build_input():
  
  # get the full name of the person entering the string
  fullname = str(input("Please enter your name: "))
  
  # get the address of the person entering the string
  address = str(input("Please enter your address: "))
  
  # get the phone number of the person entering the string
  phonenumber = str(input("Please enter your phone number: "))

  # build the full line string that will be written to file
  full_entry = fullname + "," + address + "," + phonenumber + "\n"
  
  # return the full line string
  return(full_entry)
  
# Define the main function
def main():

  # Get the filename to be working with
  filename = str(input("Please Enter the File Name: "))
 
  # open the file to either append or create the file
  file = open(f"{filename}","a")

  # write to the file from the build_input function
  file.write(build_input())

  # open the file for writing
  file = open(filename)

  # read the file to display the output
  print(file.read())

# call the main function
main()