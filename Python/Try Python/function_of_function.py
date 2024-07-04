def add(a,b):
    print(f"The addition of {a} and {b} is  :  " , a+b)
def sub(a,b):
    print(f"The substraction of {a} and {b} is  :  " , a-b)
def mul(a,b):
    print(f"The multiplication of {a} and {b} is  :  " , a*b)
def div(a,b):
    print(f"The division of {a} and {b} is  :  " , a/b)
def calculator(a,b):
    print("1 - Addition \n2 - Substraction \n3 - Multiplicaton \n4 - Division")
    n =  int(input("Enter your choice "))
    if n==1 : 
        add(a,b)    
    elif n==2 :
        sub(a,b)
    elif n==3 : 
        mul(a,b)
    elif n==4 : 
        div(a,b)
    else :
        print("Enter the choice perfectly ")  
