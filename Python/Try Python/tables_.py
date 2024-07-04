table=int(input("Enter the number for table "))
for i in range (0,11,1):
    for j in range (0,11,1):
        if j == table:
            print(f"{i} x {table} = " , j*i)
