#lambda operation (a way to create a small function)
#Use lambda when you need a function for a shorter period of time 
"""
i=10
result=lambda i : i*i
print("The result is " , result) # this prints the lambda address to use the function do below  
"""
#which is similar to 
#def function(i):
#    return i*i;
#var=function(i)
""" 
print("Square is " , result(i))
calc = lambda i: "Even number" if i % 2 == 0 else "Odd number"
print("Even or Odd by lambda ",  calc(i))
addition=lambda a,b : a+b
print("Addition by lambda" , addition(20,40))
#Lambda on list 
list1=["Akshaya" ,"Baalaji" , "Chris"]
list2=lambda list1: list1
print(list2(list1))
#squaring using lambda 
list3=[1,2,3,4,5,6,7]
list4=lambda list3 : list3*list3
print("The squared list is " , list(list4(list3)))
"""
"""
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]

list_org =[1,2,3,4,5,6,7,8,9,10]
lambdaa_filter=list(filter(lambda list1 : list1%2==0 , list_org ))
lambdaa_map=list(map(lambda list1 : list1%2!=0 , list_org ))
print(lambdaa_filter)
print(lambdaa_map)
"""
#isdigit function 
"""
strings ="Akshay"
string_int="1"
print(strings.isdigit())
print(string_int.isdigit())
lambda_work=lambda var : var.isdigit()
print("Using the lambda ")
print(lambda_work(string_int))
print(lambda_work(strings))
print("NOw for the list ")
list_of_combo=["1" , "a" , "Akshay" , "Baalaji" ,"1.4563", "C"]
print(list_of_combo)
lambda_work_detailed=list(map(lambda list1 : list1.isdigit() , list_of_combo))
print(lambda_work_detailed)
print("Same as above without lambda ")
def function (list1):
    if list1.isdigit()==1 :
        return True;
    else:
        return False
without_lambda=list(map(function , list_of_combo))
print(without_lambda)
"""
"""
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5

list_of_num=[1,2,3,4,5,6,7,8,9,10,11]
lambda_even=list(map(lambda list1: list1%2==0 , list_of_num))
lambda_odd=list(map(lambda list1: list1%2!=0 , list_of_num))
print(lambda_even)
print(lambda_odd)
result=0
def function(list1):
    global result 
    for i in range (0,len(list1),1):
        if(list1[i] == True):
            result=result+1
function(lambda_even)
print("Number of even  ",result)
result=0
function(lambda_odd)
print("Number of odd  ",result)
"""
list_1=[1,2,3]
list_2=[4,5,6]
lambda_sum=list(map(lambda x,y : x+y , list_1 , list_2  ))
print(lambda_sum)