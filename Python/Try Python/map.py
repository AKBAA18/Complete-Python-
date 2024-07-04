# mpp function has a function as a parameter and execute function in iteratable form 
import itertools
"""
list1=["Akshay", "Baalaji"]
list2=["-s","-s"]
def function(list1, list2):
    return list1+list2
list3=map(function, list1,list2)
print("Map function : ",list3)#adderss 
print("Map Working : " , list(list3))
"""
#exercise 
"""
1. Write a Python program to triple all numbers in a given list of integers. Use Python map.
list_int=[1,2,3,4,5,6,7,8,9,10]
def function_loop (list1):
    return list1*list1*list1
print("The original list " , list_int)
map_triples=map(function_loop , list_int )
print("This is the list of triples " , list(map_triples)) 
"""
"""
2. Write a Python program to add three given lists using Python map and lambda.
list1=[1,2,3,4,5]
list2=[2,3,4,5,6]
list3=[3,4,5,6,7]
list4=[4,5,6,7,8,9,10]
def function_list_add (list1,list2,list3,list4):
    return list1+list2+list3+list4    
map_func=map(function_list_add , list1,list2 ,list3, list4)
print(list(map_func))
"""
"""
3. Write a Python program to listify the list of given strings individually using Python map.
list1=["Akshaya" ,"Baalaji" , "Chris"]
def function_print(list21):
    return list21
list2=list(map(function_print , list1))
print("List copied which is similar to list1.copy() : ", list2)
#list3=list2.copy()
#print(list3)

"""
"""
5. Write a Python program to square the elements of a list using the map() function.
list1=[1,2,3,4,5,6]
def sq_func(list1):
    return list1*list1
list2=list(map(sq_func , list1))
print("Squared list is " ,list2)
#list3=sq_func(list1) cant be done  
#print(list3) when we use map we can iterate using the map function  
"""

"""
6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.
list1=['a' ,'b','c','d','e']
list3=["Akshay" , "Baalaji" "Chris" , "Deepak" , "Elavarasan"]
def function_convert(lista):
    return lista.upper()
list2=list(map(function_convert , list1))
list4=list(map(function_convert , list3))
print(list2)
print(list4)
"""
"""
7. Write a Python program to add two given lists and find the difference between them. Use the map() function.
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[10,9,8,7,6,5,4,3,2,1]
def function_add(list1, list2):
    return list1+list2
list3=list(map(function_add,list1, list2))
print("The added list " , list3)
def function_sub(list1,list2):
    return list1-list2 
list4=list(map(function_sub, list1, list2))
print("The deifference of the list is " , list4)
"""

"""
8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
convert the list and tuple to list of string 
list1=[1,2,3,4,5]
tuple1=(1,2,3,4,5)
string1=list(map(str, list1))
string2=list(map(str, tuple1))
print("List converted to string " , string1)
print("Tuple converted to string " , string2)

"""
"""

9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.
"""
"""
10. Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers.
n=50
a=0
b=1
c=0
def function_fib(i):
    global a,b,c 
    for i in range (0,i,1):
        c=a+b
        a=b
        b=c        
        print(c , end=" ")
#list1=list(itertools.islice(function_fib(n)))
function_fib(n)
# I dont know how to do with map 
"""
"""
11. Write a Python program to compute the sum of elements of an array of integers. Use the map() function.
list1=[1,2,3,4,5,6,7,8,9 , 1]
list2=list(map(lambda x: x+1 , list1)) #add one to every element 
print(list2)
sum=0
def function_sum_of_ele(lista):
    global sum 
    for i in lista :
        sum =sum+i
    return sum 
sum_of_ele=function_sum_of_ele(list1)
print("Sum of all element is " , sum_of_ele)
"""
