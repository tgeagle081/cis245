# Weather Checker
# Author: Thomas Eagle
# Class: CIS245-T303
# Assignment: Week 9 Class Project Task 2: Draft

# Import Json and Requests to pull and read API calls
import json, requests
#API key which is used multiple times for multiple requests
appid = "a04a9d82334b3701abafe963d3b7e939"

#Define the get_city function to build the api URL to get latitude and Longitude
def get_city():
  print("")
  city = str(input("Please enter the City Name: "))
  state = str(input("Please enter the 2 character state Abbreviation, example, AZ for Arizona: "))
  geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&appid={appid}"

  #get response from API and data
  response = requests.get(geo_url)
  unformated_data = response.json()

  #Data returned by the city look up comes out in a list format, need to strip it over the [] to get at the data
  cleaned_data = unformated_data[0]
  lat = cleaned_data["lat"]
  long = cleaned_data["lon"]

  # use the latitude and longitude to get tempature with the get_temp function
  get_temp(lat,long)
  
#Define the get_zip function to build the api URL with the zipcode
def get_zip():
  print("")
  zip = int(input("Please enter the Zip Code: "))
  geo_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip},US&appid={appid}"

  #get response from API and data
  response = requests.get(geo_url)
  unformated_data = response.json()

  lat = unformated_data["lat"]
  long = unformated_data["lon"]

  # use the latitude and longitude to get tempature with the get_temp function
  get_temp(lat,long)
  

#Define the get_temp function to retrieve the current and max tempature for the current day
def get_temp(lat,long):
  print("")
  url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={appid}&units=imperial"

  #get response from API and data
  response = requests.get(url)
  unformated_data = response.json()

  #get and display the current temp
  temp = unformated_data["main"]["temp"]
  print(f"The current temp is: {temp}")

  #get and display the max temp
  temp_max = unformated_data["main"]["temp_max"]
  print(f"The max temp is: {temp_max}")

  print("")
  
#Define the main function
def main():
 
  #initiate variables 
  choice = 0
 
  #while loop to allow for multiple lookups
  while choice != 3:
    print("Welcome to the Weather Report")
    print("Please One of the following options")
    print("1 Search for weather by City/State")
    print("2 Search for weather by Zip code")
    print("3 Exit Program")

    #try/except to make sure the entered item is either 1, 2, or 3
    try:
      choice = int(input("Enter your Option: "))
    except:
      print("Please enter a valid number, 1, 2, or 3")
    else:
      if choice == 1:
        get_city()
      elif choice == 2:
        get_zip()
      elif choice != 3:
        # It 1, 2, or 3 is not entered, display message and start loop again
        print("Please enter a valid number, 1, 2, or 3")

#call the main function
main()