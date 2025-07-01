# Write a function to generate Pascal's triangle up to a given number of rows.

def pascelFunc(n):

    result_list = []

    for row in range(n+1):
        arr = []

        for col in range(row+1):
            if col == row or col == 0:
                arr.append(1)
            else:
                data = result_list[row - 1][col - 1] + result_list[row - 1][col]
                arr.append(data)
        
        result_list.append(arr)
    
    return result_list



n = int(input("Enter number of rows: "))

result = pascelFunc(n)

for x in range(len(result)):

    for y in range(len(result[x])):
        print(result[x][y], end=" ")
    print("\n")