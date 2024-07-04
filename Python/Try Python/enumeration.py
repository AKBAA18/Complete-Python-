list1=["Akshay","Baalaji","Chris","Deepak","Elavarasan"]
list1.reverse()
list2=list(enumerate(list1,start=1))
print("This is the original list ",list1)
print("This is the enumerated list ",list2)
list2.sort() #this will sort based on index 
print(list2)