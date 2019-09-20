#will find total car price
#Includes all extra fees
print ("This will calculate the total price of your car")
car = input("Please enter the base price in whole dollars: ")
car = int(car)

tax = car * .07

linces = car * .01

price = car + tax + linces + 198 + 450

print ("The price of your car, including all fees, is" , price)
input("\n\nPress enter key to exit")
