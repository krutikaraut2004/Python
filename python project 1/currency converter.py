# Opening and reading the CurrencyData.txt file
with open('CurrencyData.txt') as f:
    lines = f.readlines()

# Creating a dictionary to store currency codes and their conversion rates
currencyDict = {}
for line in lines:
    # Parsing each line to extract currency code and conversion rate
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

# Taking user input for the amount to be converted
amount = int(input("Enter amount: "))

# Displaying available currency options for conversion
print("\nAvailable Options for Currency Conversions:\n")
for currency_name in currencyDict.keys():
    print(currency_name)

# Taking user input for the desired currency for conversion
currency = input("\nPlease enter one of these values: ")

# Performing the currency conversion and displaying the result
converted_amount = amount * float(currencyDict[currency])
print(f"{amount} INR is equal to {converted_amount} {currency}")
