import re 
a="The rain in Spain in in in in inThe Qkshay "
b="1 Hi Hello 23 BYe 345 tataaaaa goodbye 567567 words of India "
#findall function 
"""/*re.findall() to find all occurrences of a pattern that matches a capital letter between Q and U followed by a lowercase letter between a and n, and then followed by any word character."""
j=re.findall("[Q-U][a-n]\w+" , a) 
print("[Q-U][a-n]\w+   :",j)
j=re.findall("[Q-U][a-n]\w" , a) 
print("[Q-U][a-n]\w   :",j)
j=re.findall("[Q-U][a-n]" , a) 
print("[Q-U][a-n]   :",j)
"""
\w+ for finding till the completion of the pattern 
\w for pattern with one echarecter at the end 
noting only the pattern 
"""
c=re.findall("in"  , a)
print("in  : ",c)
#findall finds all the occurence of the pattern 
# use of raw string 
g=re.findall(r"\BT\w+",a)
print("r\BT\w+   : ",g)
"""
\B: Matches a non-word boundary. | \B matches at any position that is not at the beginning or end of a word.
T: Matches the letter 'T'.
\w+: Matches one or more word characters.
"""
h=re.findall(r"[A-T][a-z]" ,a )
print("r[A-T][a-z]   :" , h)
"""
[A-T] Starts from A to T 
[a-z] next letter can ve from a-z 
r for the rae string 
"""
i=re.findall(r"\d{3,5}\s\w.{4}",b)
print("r\d{3,5}\s\w+      :  " , i)
"""
This line finds all sequences of 3 to 5 digits followed by a space, then followed by any word character and exactly 4 characters after it in string b. The result is stored in the list i.
It had left the 23 as it needs a digit from 3 to 5 
"""
#using split 
d=re.split("\s",a)
print("split(\"\\s\",a)  : ",d)
e=re.split("\W", a)
print("split(\"\\W\",a)  : ",d)
"""
\s  :The split helps in spliting the string based on the parameter passed as the input here we have given spaces 
\W : the split is done on the Word by Word basis 
"""
#usage of sub 
f=re.sub("in","as" ,a , 3) # in converted as in string "a" and only in 3 occurences 
print("sub \(in,as ,a , 3\)   : ",f)
# use of search  
k="MIya maya Mainer Miiyer "
l=re.search(r"M[ia][yi]\w+" , k)
#find the first occurence and not the entire text 
#pattern here mentioned is start with M and next letter can be a or e and 3rd letter can be y or i and followed by the wole word matches pattern 
print("search\(r\"M[ie][yi]\w+\"\)  :" , l.group())
#group used for the merging of the found charecter 

#use of compile 
m=re.compile(r"m[ai][yi]\w+")
print("compile\(r\"m[ai][yi]\w+\"\)  " , m)
n=m.findall(k)
print("pattern is  : rm[ai][yi]\w+ and the n is m.findall " , n)
"""
re.compile() is used to compile the regular expression pattern r"m[ai][yi]\w+". The resulting compiled pattern object is stored in the variable m.
n = m.findall(k)  : This line uses the compiled pattern m to find all occurrences of the pattern in the string k using findall(). The resulting matches are stored in the list n.




"""

