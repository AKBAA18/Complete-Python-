i=10
#function for looping 
def function(n):
    for i in range (0,n,1) :
        print(i , end=" ")
function(i)
#function for binary conversion :
binary=0;
hexadecimal=0;
decimal=12312
def dec_binary_func(decimal):
    global binary
    binary=bin(decimal)
dec_binary_func(decimal)
print()
print("Decimal converted to binary :" , binary)
#hexadecimal conversion 
def dec_hexa_func(decimal):
    global hexadecimal
    hexadecimal=hex(decimal)
dec_hexa_func(decimal)
print("Decimal conversion to Hexadecimal ", hexadecimal)
#Function for list operation :
listt1=[["Akshaya" , "Baalaji "] , "Senthilraj " , 22 , "Gokulam nagar" , 612103, True]
print("List starts ")
def list_function(list1):
    print("The original list is " , list1)
    print("Index the first element " , list1[0])
    #print("The max of the list is " , max(list1)) compare on string with int is not possible 
    #print("The min of the list is " , min(list1))
    #exterd 
    list1.extend(["Maarimuthu" , "Govindhaswamy"])
    print("In function the list is " , list1)
    #extend on the list in function make the original list affected 
    #pop 
    list1.pop()
    print("The list after pop is " , list1)
    list1.reverse()
    print("The list after reverse" , list1)
    
list_function(listt1)
print("After the functions " ,listt1)
list2=["Akshay","Chris","Baalaji"] # adding annumber here makes the list min , max error 
print(min(list2))
print(max(list2))
