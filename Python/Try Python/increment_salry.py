"""
Service advisor : 20%
Suervisor 15%
mechanic 10%;
others 7%

count employee whose salary is greater than 50000 and below or equal to 50000    
if the salry is less than 0 then invalid salry 
if the employee is less tahan or equal to zero print invalid number 
"""
numofemp=int(input("Enter the number of employees "))
salary:float
name:str
desig:str
count:int
for i in range (0,numofemp,1): 
    name=input("Enter your name ")
    salary=float(input("Enter your salary " , ))
    desig=input("Enter your designation ")
    increment=0
    if desig == 'Service Advisor':
        increment=salary +((salary*20)/100);
    elif desig == 'Supervisor':
        increment=salary +((salary*15)/100);
    elif desig == 'Mechanic':
        increment=salary +((salary*10)/100);
    else :
        increment=salary +((salary*7)/100);
    print("After the increment , {0} salry is {1} " .format(name,increment) )
print("Calculation done Bye")
     
    

