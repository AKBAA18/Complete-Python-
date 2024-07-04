"""
string1="C:hello\hi\newfolder\file"
string2=r"C:hello\hi\newfolder\file" # the string is in raw format 
print(string1)
print(string2)
"""
#string formatting 
"""
c="Senthilraj"
a="Baalaji"
b="Akshaya"
print("Hi everyone my name is %s and my middle name is %s and my father name is %s "  %(b,a,c))
string = "Hi I am {1} and my middle name is {0} and my father name is {2}  "
print(string.format(a,b,c))
"""
#string methods 
#strip removes the extra whiteapaces from the staret and end 
string="    HI I am \"   Akshaya Baalaji Senthilraj    \" I am working as an Engineer in Tata Elxsi      "
print("Stripped string ",string.strip())
print("Normal String ",string)
#len  
print("Length of string " ,len(string))
#string to upper case 
print("The string converted to upper case ", string.upper())
#string to lower case 
print("The string converted to lower case " ,string.lower())
#Replace 
print("Replace I with II " ,string.replace('I' , 'II'))
#Split 
print("Spliting done " , string.split())
#starts with 
print("Starts with HII " ,string.startswith("HII"))
#ends with 
print("Ends with Elxsi " ,string.endswith("Elxsi"))#false because of space inbetween 