#control structure if elif else 
"""
a=int(input("Enter a number     "))
if(a%2==0):
    print("Even")
elif(a%2!=0):
    print("ODD");
else:
    print("Enter the number correctly ")
"""
#control structure for 
n=int(input("ENetr a number of start for making the star pattern "))
"""
for i in range (1,n+1):
    #print(i) 1 2 3 4 5 
    for j in range (0,i): # j = 0 1 2 3 4 when i =5 
        print("*" , end =" ")
    print()
*
* *
* * *
* * * *
* * * * *
"""
"""
for i in range (n,0,-1):
    for j in range (0,i):
        print("*" , end =" ")
    print()
* * * * *
* * * *
* * *
* *
*
"""
"""
for i in range (1,n+1):
    for j in range (0,i):
        print(" " , end =" ")
    for k in range (n+1, i ,-1):
        print("*" , end =" ")
    print()
  * * * * *
    * * * *
      * * *
        * *
          *
"""
"""
for i in range (1,n+1):
    for j in range (0,i):
        print(" " , end =" ")
    for k in range (n+1, i ,-1):
        print("*" , end =" ")
    for l in range(n+1 , i+1,-1):
        print("*" , end=" ") 
    print()
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          * 
"""
#control structure while 
while n<20:
    print(n, end= " ")
    n=n+1

print(n)