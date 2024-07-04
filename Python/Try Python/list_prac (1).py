listt=[1,True,"Akshaya Baalaji" , False , 45.3435, 'g']
print(listt)
#slicing and indexing 
for index , elements in enumerate(listt):
    print(f"Index {index} : {elements}");
"""
enumerate :
Enumerate is Python built in function  
return a tuple containg index and element in list 
f - is the formateed string in latest pattern 
"""
listt[1:2] = [] #this removes the index 1 
print(listt);
print();
#list functions 
print("Length of list " , len(listt)); #Len return the lenght of list 
print("Append 2 " , listt.append(2) );#append will add a element at last 
print("List after function performed " , listt);
print("Remove 1 " , listt.remove(1)); #This removes the last element from the list 
print("List after function performed " , listt);
print("Pop : " , listt.pop());#This deleted the last element from the list 
print("List after function performed " , listt);
print("Insert " , listt.insert(1,True))
print("List after function performed " , listt);
print("Count \"Akshaya Baalaji\" " ,listt.count("Akshaya Baalaji"))
print("Reverse ",listt.reverse())
print("List after function performed " , listt);
print("Extend [Viji , True , 0 , False ] ",listt.extend(["Viji" , True , 0 , False ]))
print("List after function performed " , listt);
#Shared list 
slist=listt
print("The slist is the shared list of list " ,slist)
#pop an element from listt to see it reflect on slist
listt.pop()
print("Original list after pop" , listt)
print("Shared list after pop " , slist)
#pop an element from slist to see it reflect on listt 
slist.pop()
print("Original list after pop" , listt)
print("Shared list after pop " , slist)

print("Clear ", listt.clear()); #This clears all content but the list remains 
print("List after function performed " , listt);
"""
[1, True, 'Akshaya Baalaji', False, 45.3435, 'g']
Index 0 : 1
Index 1 : True
Index 2 : Akshaya Baalaji
Index 3 : False
Index 4 : 45.3435
Index 5 : g
[1, 'Akshaya Baalaji', False, 45.3435, 'g']

Length of list  5
Append 2  None
List after function performed  [1, 'Akshaya Baalaji', False, 45.3435, 'g', 2]
Remove 1  None
List after function performed  ['Akshaya Baalaji', False, 45.3435, 'g', 2]
Pop :  2
List after function performed  ['Akshaya Baalaji', False, 45.3435, 'g']
Insert  None
List after function performed  ['Akshaya Baalaji', True, False, 45.3435, 'g']
Count "Akshaya Baalaji"  1
Reverse  None
List after function performed  ['g', 45.3435, False, True, 'Akshaya Baalaji']
Extend [Viji , True , 0 , False ]  None
List after function performed  ['g', 45.3435, False, True, 'Akshaya Baalaji', 'Viji', True, 0, False]
The slist is the shared list of list  ['g', 45.3435, False, True, 'Akshaya Baalaji', 'Viji', True, 0, False]
Original list after pop ['g', 45.3435, False, True, 'Akshaya Baalaji', 'Viji', True, 0]
Shared list after pop  ['g', 45.3435, False, True, 'Akshaya Baalaji', 'Viji', True, 0]
Original list after pop ['g', 45.3435, False, True, 'Akshaya Baalaji', 'Viji', True]
Shared list after pop  ['g', 45.3435, False, True, 'Akshaya Baalaji', 'Viji', True]
Clear  None
List after function performed  []
    """

listy[5]
print(listy)

