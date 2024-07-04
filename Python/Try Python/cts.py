from functools import reduce
"""print("Hi")
t=1
country=[]
noofsat=[]
srate=[]
while (t) :
    a=input("Enter the country")
    country.append(a)
    b=int(input("ENter the number of satellite launched "))
    noofsat.append(b)
    c=int(input("Enter the successrate "))
    srate.append(c)
    #global t 
    t=int(input("To enter another data press 1 or else 0 "))
for i in range (0,len(country),1):
    print(country[i] , " successfully launched " , noofsat[i] , " and the success rate is " , srate[i])
"""
"""
print("Hi")
t=1
i=0
while (t) :
    a=int(input("Enter the count of people "))
    b=int(input("Single dose count "))
    c=int(input("Double dose count "))
    #global t 
    d=a-(b+c)
    print("Not vaccinated people count : " , d)
    e=((c)/a)*100
    print("The percentage of people vaccinated are " , round(e,2))
    t=int(input("Do you want to continue 1 for yes and 0 for no  "))
"""
"""
sabove=0
sbelow=0
t=1
while (t):
    a=int(input("Enter no of employees "))
    
    for i in range (0,a,1):
        b=input("Employee name ")
        c=int(input("Salary "))
        d=input("Designation ")
       
        if c >50000 : 
            sabove = sabove+1
        else:
            sbelow=sbelow+1            
        if d in 'Service Advisor' : 
            profit=(c*20)/100
            inhand=c+profit
        elif d in 'Supervisor':
            profit=(c*15)/100
            inhand=c+profit
        elif d in 'Mechanic':
            profit=(c*10)/100
            inhand=c+profit
        elif d in 'Mechanic':
            profit=(c*7)/100
            inhand=c+profit
        else:
            print("Entered wrong bye ")
        print("After the increment " , b , " salary is " , inhand)
    t=int(input("Enter either 1 to continue and 0 to end "))
    print("Employee count :" , a)
    print("Salary above 50000 is " , sabove)
    print("Salary below or equal to 50000 is " , sbelow)
    sabove=0
    sbelow=0
"""
"""
e=int(input("Enter the total units consumed "))
cost=0
if e <=50 and e>=0:
    cost=.50*e
    final=round(cost,2)
elif  e >=50 and e <=150:
    cost=.75*e
    final=round(cost,2)
elif  e >=150 and e <=250:
    cost=1.20*e
    final=round(cost,2)
elif  e >=250 and e <=500:
    cost=1.50*e
    final=round(((cost*20)/100) + (cost) )
else:
    final=0
if final==0 : 
    print("Invalid unit ")
else:
    print("Electricity bill is " , final)
    
"""
"""
a=1
attempt=0
slist=[]
while a >0 :
    b=int(input("Scores "))
    slist.append(b)
    attempt=attempt+1
    c=b
    while (c<100) : 
        b=int(input())
        slist.append(b)
        c=reduce(lambda x,y : x+y , slist)
        attempt=attempt+1
    a=0
print("Enter the number of attempt " , attempt)
"""
"""
t=1
total=[]
while (t):
    a=int(input("Caramel ice cream "))
    b =int (input("Bubble Gum Ice Cream "))
    c=int(input("Strawberry ice cream "))
    d=int(input("Cookies and Cream "))
    print("Caramel ice cream")
    print("Cost : 30 " )
    print("Quantity " , a)
    e=30*a
    print("Total Amount  :$" , e)
    total.append(e)
    e=0
    print("Bubble Gum Ice Cream ")
    print("Cost : 20 " )
    print("Quantity " , b)
    e=20*a
    print("Total Amount  :$" , e)
    total.append(e)
    e=0
    print("Strawberry ice cream")
    print("Cost : 10 " )
    print("Quantity " , c)
    e=10*a
    print("Total Amount  :$" , e)
    total.append(e)
    e=0
    print("Cookies and Cream ")
    print("Cost : 15 " )
    print("Quantity " , d)
    e=15*a
    print("Total Amount  :$" , e)
    total.append(e)
    e=0
    f=reduce(lambda x,y : x+y , total)
    g=int(input("Enter 0 for stopping and 1 for continuing and 2 to find total"))
    if(g==1):
        t=1
    elif(g==0):
        t=0
    else:
        print("The total amount is " , f) """
        
st=[]
li=[1,2,3,4,5,8,3,5,1,1,2,3,4,5,7,8,1,2,3,4,6,6,6,5,1,7]
for i in range (65,91,1):
    a=chr(i)
    st.append(a)
print(len(st))
print(len(li))
name=input("Enter the name ")
i=0
luckynum=0
for i in range (0,len(name),1):
    temp=st.index(name[i])
    luckynum=li[temp] + luckynum
print( "Your lucky number is : ",luckynum)
