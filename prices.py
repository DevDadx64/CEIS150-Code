
# Programmer: Miller Emion
# Date: 02/10/2021
# Assignment: price.py

# Purpose: This program will ask the user to enter the minimum price and the employee's name.

# initialize count variable 

count = 0

# initialize sum variable

sum = 0

# input employee name

employeeName = input("Please enter the employee's full name: ")

# input min_price and conver to a float

min_price = float(input("Please enter the minimum price: "))

#create a list of price examples

price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8,
79.3, 101.2]

# loop through the list and output the prices greater than the min_price

for price in price_list:
    sum += price
    if price > min_price:
        count += 1
print("Hello " + employeeName + ", the minimum price is ", min_price, ".")
print("There are", count, "prices greater than the minimum price.")
print("The total price is", sum, ".")

