import re
a="The rain in Spain in in in in inThe "
b="1 Hi Hello 23 BYe 345 tataaaaa goodbye 567567 words of India "
#findall function
j=re.findall("[Q-U][a-n]\w" , a)
c=re.findall("in"  , a)
# use of raw string
g=re.findall(r"\BT\w+",a)
h=re.findall(r"[A-T][a-z]" ,a )
i=re.findall(r"\d{3,5}\s\w.{4}",b)
"""
can start from Q - U
and the next letter can be from the a - n     
"""
print("[Q-U][a-n]\w   :",j)   
print("in  : ",c)
print("r\BT\w+   : ",g)
print("r[A-T][a-z]   :" , h)
print("r\d{3,5}\s\w+      :  " , i)
#using split
d=re.split("\s",a)
e=re.split("\W", a)
print("\s   : ",d)
print("\W   : ",e)
#usage of sub
f=re.sub("in","as" ,a , 3) # in converted as in string "a" and only in 3 occurences
print("in,as ,a , 3   : ",f)
# use of search
k="MIya maya Maiyer Mainer"
l=re.search(r"M[ae][yi]\w+" , k)
print("rM[ae][yi]\w+   :" , l.group())
#use of compile
m=re.compile(r"m[ai][yi]\w+")
n=m.findall(k)
print("pattern is  : rm[ai][yi]\w+ and the n is m.findall " , n)