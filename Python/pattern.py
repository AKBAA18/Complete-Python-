# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:46:25 2024

@author: aksha
"""

#This is the comment 
"""
This is the long line comment 
"""
#print("Hello" +   " " + "World")
""""
name="Akshaya baalaji"

print(name[0]) #indexing
print(name[-1])#negative indexing 
print(name[0:4])#slicing 
print(len(name))#size 
print("A" in name)#membership operator used here """

"""
i=10;
def myfunction():
    global i 
    print(i , " ")
    i=i-1
myfunction();
print(i);
print("\n")
for j in range (i,0,-1):
    print(j, " " )
"""
#pattern 1 
n=int(input("Enter the input "))
for i in range (0,n+1):
    for j in range (0,i):
        print("*" , end=" ")
    print()
"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""
#patern 2 
print()
for i in range (0,n+1):
    for j in range (n,i,-1):
        print("*" , end=" ")
    print()
    
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:50:06 2024
print("HI")
for i in range (5,0,-1):
    print(i)
    for j in range (0,i):
        print(j, end =" ")
    print()
print("Bye")



@author: aksha
"""
