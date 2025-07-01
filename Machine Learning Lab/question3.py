# Write a program to calculate the sum of all even numbers from 1 to 100 with for and while loop.

sum = 0

for x in range(1, 101):
    if x % 2 == 0:
        sum = sum + x

print(f"Sum using for loop: {sum}")

y = 1
sum = 0
while y <= 100:
    if y % 2 == 0:
        sum = sum + y
    y+=1

print(f"Sum using while loop: {sum}")