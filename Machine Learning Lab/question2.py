#Create a program that calculates the discount amount based on the purchase amount.
#If the purchase amount is greater than $100, apply a 10% discount; otherwise, apply a 5% discount.

x = float(input("Enter the purchase amount: "))

if x > 100:
    dis_price = x - (x * 0.1)
else:
    dis_price = x - (x * 0.05)

print(f"Discount price: {dis_price}")