"""
Question 3
Write a program that will take one string as input. The program will then remove vowels a, e, i, o, and u (in lower or upper case ) from the string. If there are two or more vowels that occur together then the program shall ignore all of those vowels.

Example 1

Input:  Cat
Output:  Ct
"""
strings=input("Enter a string to remove vowel ")
temporary_string=""
for i in strings:
    if i not in ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U'] :
        temporary_string=temporary_string+i

print("Original string : " , strings)
print("Removed string : " , temporary_string)
    