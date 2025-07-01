# Write a recursive function to calculate x raised to the power of n. Input: x = 2, n = 3; Output: 8

def calcPower(x, n):
    if n == 0:
        return 1
    if x == 0:
        return 0
    
    return x * calcPower(x, n - 1)


x = int(input("Enter x: "))
n = int(input("Enter n: "))

result = calcPower(x, n)
print(result)