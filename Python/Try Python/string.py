string1 
"""
#string comparision 
string1="Akshaya Baalaji"
string2='Akshaya Baalaji Senthilraj'
if(string1 == string2):
    print("Both are same compared by == assignment operator ")
if(string1 != string2):
    print("Both are Different compared by != assignment operator ")    
if(string1 is string2):#here the identity operator compare the both string1 and string2 whether all charecters are same in string1 and string2 
    print("Both are same compared by is identity operator ")
if(string1 is not string2):
    print("Both are Different compared by is not identity operator ")
if(string1 in string2): # here the membership operator compare the the first char of string1 and second char of string 2 till the end of string1   
    print("Both are same compared by in membership operator")
if(string1 not in string2):
    print("Both are Different compared by not in membership operator")
"""
