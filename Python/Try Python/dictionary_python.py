dictt={"Name":"Akshaya Baalaji " , "Age" : 21 , "Phno " : 9361486996 , "Sex " : "Male" ,"Address" : "22 \"Gokulam nagar \" Second cross "}
print(dictt)
#length of the dictionary 
print("Length of the dict " , len(dictt) )
#iterate 
for keyy , value  in  dictt.items():
    print("Key - " , keyy ,end =" " )
    print("   Value - ", value)
#Copy the dictionary
dictt2=dictt.copy();
print("The copied dictionary is ",dictt2)
#Fromkeys function 
keys=["Dist" , "State" , "Pincode"]
values=["TNJ" , "TN" , "612103"]
new_dict=dictt.fromkeys(keys,values)
print("New dict created by from keys " , new_dict)   
#get values 
print("The address is fetched by get function  ", dictt.get('Address'))
#.items function 
print("The dict print by dict.items() " , dictt.items())
#from keys make list 
key_list=dictt.keys()
print("The list from the keys of dict ", key_list)
#from values make list 
values_list=dictt.values()
print("The list from the values of dict ", values_list)
#pop with key deletes it 
deleted_ele= dictt2.pop("Address")
print("The deleted element is " , deleted_ele)
print("The dictionary after pop  " , dictt2 ) 
#popitem deleted the last element 
dictt2.popitem()
print("The dict after the popitem " , dictt2)
#update the value in dictt2
dictt2.update({'Phno' : 9342083665})
print("The dict after the update " , dictt2)
#clear : deleted all data 
dictt2.clear()
print("The dictt2 is cleared " , dictt2)
print("Only the data is cleared the dict remains ")


    
    