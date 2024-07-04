"""
Write a program that will print the sum of diagonal elements of a 10X10 matrix. The program will take a total of 100 numbers as input (10 numbers will be input per line and each number will be separated by a space).

Example 1

Input:         1 2 3 4 5 6 7 8 9 0 
               0 1 2 3 4 5 6 7 8 0
               3 4 5 6 7 8 9 6 4 0
               2 3 4 5 6 7 8 9 3 2
               3 4 5 6 7 4 3 2 1 3
               3 4 5 6 2 4 4 2 4 6
               2 3 4 6 2 4 6 2 3 5
               2 3 5 6 2 4 6 2 3 5
               2 4 6 2 1 4 3 3 5 2
               3 3 5 2 4 6 2 1 4 6
Output:  42
"""
rows , columns =5 , 5 
array = [[0,1,2,3,4] ,[0,1,2,3,4] ,[0,1,2,3,4] ,[0,1,2,3,4] ,[0,1,2,3,4] ]# for creating a array with row and column 
integer=0
"""
for i in range (0,rows,1):
    for j in range (0,columns,1):
        print(array[i][j]," " , end=" ")
    print()
"""
for i in range (0,rows,1):
    for j in range (0,columns,1):
        integer=int(input("Enter the array element  "))
        array[i][j]=integer
#for printing the code 
for i in range (0,rows,1):
    for j in range (0,columns,1):
        print(array[i][j]," " , end=" ")
    print()

#for diagonal element sum calculation 
sumis=0
for i in range (0,rows,1):
    for j in range (0,columns,1):
        if(i==j):
            sumis=sumis+array[i][j]

print("The sum is of the diagonal is "  , sumis)
