'''
Write a program to create a dictionary where the keys are numbers from 1 to n and the values are their squares.
Input: n = 5
Output:
{    1: 1,   
2: 4,    
3: 9,    
4: 16,    
5: 25
}
'''
n = int(input("Enter the number of data: "))
my_dict = {}

for x in range(1, n+1):
    my_dict[x] = x**2 #square of the key

print(my_dict)