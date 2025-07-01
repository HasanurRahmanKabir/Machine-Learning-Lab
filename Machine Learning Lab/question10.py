# Write a function to convert a decimal number to its binary representation.

def decToBin(n):
    res = ""

    while n > 0:
        res = str(n & 1) + res
        n >>= 1

    return res

x = int(input("enter the number: "))

print(decToBin(x))