# Stocker Ticker Lookup
# Author: Thomas Eagle
# Class: CIS245-T303
# Assignment: 7.1

#create dictionary of Stock Symbols and prices
stocks_dict = {
  "IBM": "102.34",
  "WMT": "148.22",
  "ATVI": "92.35",
  "MSFT": "247.23",
  "TSLA": "178.97",
  "META": "151.65",
  "AMC": "5.37",
  "GME": "22.58",
  "DIS": "109.45",
  "AAPL": "145.98"
}

#define main function
def main():
  # Ask for input for the stock symbol
  lookup = input("Please enter your stock symbol:")
  # Use Try/Except to catch errors for non-valid Stock Symbols
  try:
    #look up price associated with Stock Symbol
    price = stocks_dict[lookup]
    #print Stock symbol and the price
    print("The Stock price for", lookup, "is current $",price)
 
  except:
    #exception message and recall to main to allow relook up
    print("That is not a valid stock symbol. Please enter a valid stock symbol")
    main()

#define lists of valid stocks to know what Symbols are accepted
def list_stocks():
  print("Valid Stock Symbols:")
  print("IBM for IBM")
  print("WMT for Walmart")
  print("ATVI for Activision Blizzard")
  print("MSFT for Microsoft")
  print("TSLA for Tesla")
  print("META for Meta Platforms")
  print("AMC for AMC Entertainment")
  print("GME for Gamestop")
  print("DIS for Disney")
  print("AAPL for Apple")
  print("--")

#call list of stocks first to always show on top, followed by main to look up stock symbols
list_stocks()
main()