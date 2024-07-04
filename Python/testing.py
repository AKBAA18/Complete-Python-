# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:07:32 2024

@author: aksha
"""
"""
listowner=["A","B" ,"C"]
list1=[1000,2000,3000]
list2=[100,200,300]
list3:list=[0,0,0]
for i in range (0,len(list1),1):
    for j in range (0,len(list2),1):
        if(j==i):
            list3[i]=list1[i]+list2[i]
            print(f"The salry of {listowner[i]} is {list3[i]}")
print(list3)
list4=list3.reverse()
print(list3)
print(list4)
#sort and the  reverse = true for the descending order sorting 
#sort and the reverse = flase forr the ascending order sorting 
list3.sort(reverse=False)
print(list3)
"""
"""
n = int(input())
for i in range (0,n,1):
    print(i*i)
"""
def is_leap(year):
    leap = False
    if year%4==0 and year%100==0 :
        leap = True
        return leap
    else :
        leap = False
        return leap
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))