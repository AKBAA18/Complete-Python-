"""a,b,c=1,2,3
print(a)
print(b)
print(c)
strings="Hi BYe"
#print(strings + a);# error because of strongly typed prog language 
aa=str(a)
print(strings + aa);
#isinstance usage 
if isinstance (aa,str):
    print("It is a string daatype")

number=1000
string_num = str(number)
float_num=float(number)
#char_number=char(number)
list_number=list(string_num)
tuple_number=tuple(string_num)
set_number = set(string_num)
#dictionary_number=dict(number )


print(string_num)
print(float_num)
print(list_number)
print(tuple_number)
print(set_number)
#print(dict_number)
"""
"""
#this will be string by default 
number=input("Enter a String or NUmber ")
print(type(number))
#so type cast 
number1=int(input("Enter the number because it is type casted at time of input itself "))
print(type(number1))
"""
"""
n=input("Enter the input ")
add=10
summ=add+n if isinstance (n, int) else int(n)+add
print("Your addition is " , summ)

#format example 1 (Hardcoring a variable )
strings="ENter your name {name} and your age {age}".format(name="Akshay" , age=34)
print(strings)

#format example 2 (psasing the parameter as the prev variables )
fname="Akshaya Baalaji"
page=21
strings="Hi {name} and your age {age}".format(name=fname , age=page)
print(strings)
"""
"""
age=12
fname="Akshaya baalaji"
strings=f"Hi {0} your age is {0}"

print(strings)
#string is a iterable type and 
#it is a collection of charecter in sequence 

"""

"""
name ="AKshaya Baalaji "
namename:str="1"
print(name)
print(namename)
#type casting on integer 
print(int(namename))
"""
"""
number:str=9
print(type(number))
"""
"""
salary=12323
bin_bytes=bytes(salary)
print(bin_bytes)

"""
"""
mark=199
total_mark=400
internal=100
consolidate=mark+internal if(mark >200) else mark

print(consolidate)


"""
"""
string="Akshaya Abaalaji sdjfuysdg Akshaya aihisdf iif  iuhif iyf "
list_of_str=list(string)
print(list_of_str)
string_spli=list(string.split(" "));

print("Till end of the string " , string_spli)
string_spli=list(string.split(" " ,2));# 2 is the index till we need to split 
print("Till the secone index ",string_spli)
#on above the split will be done for the first 2 index and make the remaining content in 3third index 
print(string.capitalize())

print(string.title())

string_new="I am {3} and I am from {2} and I am specialized in {1} and my age is {0}"
print(string_new.format(21,"Bigdata","TNJ","Akshaya Baalaji"))

print(string.replace("Akshaya", "AAkshaya"));

print(string.replace("A", "X",2));

print("Count ..............")
print(string.count("A"));
print(string.count("A",0,9));
#the above count we are mentioning the index where to start and end the count of occurence 


print("Strip....................")
print(" a b c d    ".strip()) # remove leading and trailing white spaces 
print("      a b  c  d    ".rstrip()) # remove the spaces at the end 


a=10
print(a.__lt__(11)) #true 

import math # module from which we are going to use function 
floatvar=100.34
print(floatvar.__floor__())

inputt=int(input("Enter a number "))
if(inputt==0):
    print("Zero")
elif(inputt==1):
    print("One")
elif(inputt==2):
    print("Two")
elif(inputt==3):
    print("Three")
else :
    print("SOme other numbers ")
"""
"""
#using list built in functions 
make_list=[a,b,c] # making the list from the variables 
print(max(make_list));
#we can take the greatest by sorting and taking the last element in list 
make_list.sort(); #sort will sort the list 
print("Taking the last elemrent from the list ",make_list[-1])
"""
"""
#using simple conditional structure 
a=10
c=10
b=30
if a==b and a==c :
    print("All are same ")
elif a>=b and a>=c :
    print(a, " is the greatest ")
elif b>=a and b>=c :
    print(b, " is the greatest ")
else :
    print(c, " is the greatest ")
"""    
"""
#using nested conditional structure 
a=10
b=10
c=30

if a==b and b!=c:
    if a>=b and a>=c :
        print(a , " is the greatest ")
    elif b>=a and b>=c :
        print(b," is the greatest ")
    else :
        print(c , " is the greatest ")
else :
    print("All are same ")

"""