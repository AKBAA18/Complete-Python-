from functools import reduce 
import random 
"""#program to print mul of 3 and 5 
a=int(input("Enter a number which is greater than 50 "))
b=[]
c=[]
d=[]
for i in range (1,a) :
    if(i%2==0) : 
        d.append(i)
    elif(i % 3==0  ):
         b.append(i) 
    elif(i % 5==0):
         c.append(i) 
    else : 
        continue
print("Multiple of 3 is " ,b)
print("Multiple of 5 is " ,c)     
#Sum of all element in a list by lambda function 
print("Sum of all even element in a list ")
e=reduce(lambda x,y :x+y , d)
print(e)"""
"""
# random number generation 
a=random.randint(1,10)
print("Random integer between 1- 10",a)
b=[1,23,4,45,45,656,56,43]
random.shuffle(b)
print("The b is shuffled ",b)
c=random.choice(b)
print("Choosing a choice from a list ",c)"""
#factorial by while loop 
"""
a=int(input("Factorial generation enter a number "))
fact =1
i =1
while a>i :
    fact=fact*i
    i=i+1
print(fact)"""
"""
#palindrome checker 
str=input("Enter a string ")
ref=""
for i in range (len(str)-1,0,-1):
    ref=ref+str[i]
print("The reversed string is ", ref )
"""
#printing sqa of num using map 
"""
a=[1,2,3,4,5,6,7,8,9,10]
b=list(map(lambda x: x*x , a))
print(b)
"""
#number of vowels in a string 
"""
a=input("ENter a string ")
b=0
for i in range (0,len(a),1):
    if (a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u' ):
        b=b+1
print("The number of vowels in string  " , a , "is " , b)
"""
"""
#
b = []
a = int(input("Enter the number: "))
for i in range(1, a, 1):
    b.append(random.randint(1, 100))
print("The list is", b)
def avg(x):
    return x / 2
# Map the avg function to each element in the list
e = list(map(avg, b))
print("The modified list is", e)
d=map(lambda x,y : str(x) + " " + str(y) , b,e)
print(list(d))
"""
"""
#use of reduce 
b=[]
a=int(input("Enter the number of list element "))
for i in range (1,a,1):
    b.append(random.randint(1,100))
print("The random list is " , b)
c=reduce(lambda x,y : x+y ,b)
print(c) """
#prime number 
"""
b = []
a = int(input("Enter the number: "))
for i in range(1, a, 1):
    b.append(random.randint(1, 100))
print(b)
def func(b):
    for i in range(2,int(b/2)+1):
        if b % i ==0 :
            break 
        else :
            return b
c=map(func , b)
print(list(c))
"""
#using reducer split by odd and even 
"""
b=[]
a=int(input("Enter the number of list element "))
for i in range (1,a,1):
    b.append(random.randint(1,100))
print("The random list is " , b)
c=list(filter(lambda x : x%2==0 , b))
print(c)
d=list(filter(lambda x : x%2!=0 , b))
print(d)
"""
"""
#length of string 
b=[]
a=int(input("Enter the leng of list"))
for i in range (1,a):
    b.append(random.randint(1,100))
print(b)
c=sorted(b)
print(c)
"""
try :
    a='2'+2
except Exception as e :
    print("Error arraises here ")