#filter function filters the record based on the condition  
"""
#this is the list filtered only the odd element  
list1=[1,2,3,4,5,6,7,8,9,10]
list2= list(filter(lambda s : (s%2==0) , list1 ))
print("filtered List is ",list2) 
#understanding the string 
string1="Akshayabaalaji"
list_string=string1.split(" "); #searches for space 
list_string_conversion=list(string1)#directly convert to LIST fROm string   
print(list_string_conversion) 
print("The string converted to list_string is " , list_string)
def func_vowel(list1):
    if list1 in ['a' , 'e' , 'i' , 'o' , 'u'] : 
        return True
    else :
        return False
list3=list(map(func_vowel, list_string_conversion)) #map is used for mapping to list  
list4=list(filter(lambda list : list in ['a' , 'e' , 'i' , 'o' , 'u'] , list_string_conversion))
print(list3)
print(list4)
#Write a Python program that creates a 
#list of names and uses the filter function to extract names that start with a vowel (A, E, I, O, U).
"""
"""
10. Write a Python program that implements a Python program 
that filters out dates (in the format "YYYY-MM-DD") that are in the future using the filter function.

date="2024-12-12"
print("String is : " , date)
splitt=date.split("-")
print(splitt)
filter_prg=list(filter(lambda s: s.split("-") , date ))
print(filter_prg)
"""




