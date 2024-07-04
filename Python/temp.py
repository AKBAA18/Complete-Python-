import fibo 
x=int(input("Enter a number "))
y=int(input("Enter a number "))
z=int(input("Enter 1 for add \nEnter 2 for sub \nEnter 3 for mul \nEnter 4 fro div \nEnter 5 fro rem "))
result =0
if z==1  :
    result=fibo.add(x,y)
    print("Added " , result)
elif z==2 : 
    result=fibo.sub(x,y)
    print("Sub " , result)
elif z==3 : 
    result=fibo.mul(x,y)
    print("Mul" , result)
elif z==4 : 
    result=fibo.div(x,y)
    print("Div" , result)
elif z==5 :
    result=fibo.rem(x,y)
    print("Remainder " , result)
else :
    print("Enter the number correctly ")     