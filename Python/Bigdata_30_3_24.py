"""
BigData notes 30/3/24

Conditional structure

for is a unconditional looping 
for i  in range (0,10,1): #these are iterable 
    
simple example 
listt=[1,2,3,4,5]
print(listt)
#add one in the list 
#for that we have to iterate the list so that we can add +1 
for i in range (0,len(listt),1):
    listt[i]=listt[i]+1

print (listt)

(and )

while is a conditional looping 
while i<10:
    print(i)
    i++



NOTE :
    Strings can be iterated 
    
Python loop :
    while  # in python there is no do while 
    for
    
Constructs / classes :
    Continue :
        pass the current iteration and continue with the next iteration 
        
        
    Break :
        break is used to break frm the looping structure 
        if it is inside the if it breaks the loop above the if 
    
    
    exit :
        similar to break exit from the entire program 
        
Bigdata 06/4/24 

How to  implement do while in python :
    while True :
        print("This is always true ")
        if True :
            break;

Datatype 

Collection type :
    Group of elements can be accessed using ssome way the hold the list value in 3rd dimension 
            or
    A group / collection / list of elements / collection can be organized , accessed using index , key , position 

Different types : Arranged based on the priority 
    1.List   []
    2.Dict   {}
    3.Tuple   ()
    4.Set   {}
    
Before types understand Below definitions :
    Iterable (looping ) 
    mutable (changable) 
    updatable (modifyable )
    resizable (add/delete element ) 
    accessable (using index , position ,value , size ) 


Why complex type :
    To manage / store / parse complex data , work on semi structure data 


List :
    List are Iterable (looping ) , mutable (changable) , updatable (modifyable ), resizable (add/delete element ) ,accessable (using index , position ,value , size ) 
    List elements can be either homogenous / heterogenous 
    list : elements are identified by index 
        Ex   ["Akshay " , 12 , "Baalaji" ]
        index    0         1       3          
    index always starts from 0 negative index is accessed by the the len(list)-1
    Ex :
        listq=["Ajds",98,"3e"]
        print(listq)
        print(listq[-1])
        print(len(listq))
        print(listq[len(listq)-1])
    In BigData :
        List can be used to store the column data 
Dict :
    Ex :
        dict_var={1:"Akshay" ,2:"Baalaji" }
        print(dict_var.get(2))
    Elements in list will be key value paired 
    Dictionary can be accessed by key ,values 
    In BigData :
        Dict can be used to store a column with key value  (column name and value )
        

Tuple :
    Ex :
        tuple_var=("Akshay " , 12,"Baalaji")

    Tuples are similar to list and these are heterogenous 
    Tuples are immutable this is the differnce between list and tuple 
    Tuples are accessed by index 
    In BigData :
      Tuple is used to store one record (row)
     
Operation and its possibility :
    resizable :
        tuple1 = (1,"Akshay" , 23 , "Baalaji")
        tuple2 = (23,"Baalaji ")
        #tuple1.__add__(45,56) #cant alter the size of the tuple 
        #rather we can do 
        tuple3 = tuple1.__add__(tuple2)   
        print(tuple3)
    
    changable :
        #tuple1[0] = 45 
        #we cant change the tuple 
        
    delete :
        #tuple1.__remove__(45)
        #we cant delete the element of the tuple 
    
    
    To do all these we have to convert tuple to list and 
    use the list to do all modification and change it to tuple 
    
    Ex :
        tuple1 = (1,"Akshay" , 23 , "Baalaji")
        tuple2 = (23,"Baalaji")
        #tuple1.__add__(45,56) #cant alter the size of the tuple 
        #rather we can do 
        tuple3 = tuple1.__add__(tuple2)   
        print(tuple3)
        tuple4 = tuple3.__delattr__(self , "Baalaji")
        print(tuple4)
        
    practical :
        tuple1 = (1 , 1 , 2 , 2 , 3 , 3 , 4 , 5 , "Akshaya Baalaji" , "Senthil raj" , True , False )
        tuple2 = (23,"Baalaji")
        print("Tuple 1 : " , tuple1)
        print("Tuple 2 : " , tuple2)

    #resizable : rather we can create a new tuple and add the element 
        #tuple1.__add__(45,56) #cant alter the size of the tuple 
        tuple3 = tuple1.__add__(tuple2)   
        #or 
        tuple4 = tuple1 + tuple2 
        print("Tuple 3 = Tuple1.__add__(Tuple2) : ",tuple3)
        print("Tuple 4 =  Tuple 1 + Tuple 2  : ",tuple4)
    
    #changable :  we cant change the tuple 
        #tuple1[0] = 45 
     
    #delete :   we cant delete the element of the tuple
        #tuple1.__remove__(45)
        
        element_to_remove = 2
        #as the tuple is not mutable we must create a new tuple and reomve the element 
        tuple5 = tuple(item for item in tuple3 if item != element_to_remove)
        print("Tuple 5 = Remove 2 from the tuple 3 : ",tuple5)
        
Set :
    Ex:
        set_var={1,2,3,0,True , false , "Akshay" , "Akshay"}
        print(set_var)
        
    Set will hold the data in sorted and deduplicated fashion 
    Cant be accessed using index and can be accessed by using values 
    Set elements are immutable 


    Practical :
        sett=({1,2,-1,3,4,5,1,2,3,4,5,6,0,True,False})
        print(sett) # sert automatically identifies the deplicate and remove it 

        #iterable 

        sett.add("baalaji")
        print("Set after append " , sett)

        sett.remove(1)
        print("Set after remove " , sett)

        sett.pop()
        print("Set after popping " , sett)


        #extend : We cant do a extend operation on the set

            #list2=[12,23,34,45]
            #sett.extend(list2)
            #print("After extending " , sett)

        #alternative for extend 

        set3={12,23,34,56,67,1,2,3}
        set_result=sett.union(set3)
        print("After the union operation  " , set_result)

        # in prev the not common data wont be updated 

        set_result = sett.intersection(set3)
        print("After the intersection operation  " , set_result)

        set_result = sett.intersection_update(set3)
        print("After the intersection_update operation  " , set_result)

    practical 2 :
        
        set1={2,3,4,5,6,True,False , 0 ,1 ,23 , 34 , 45 , 56 , 67 ,78 , 89 ,10 ,"Akshaya" , "Baalaji" }
        print(set1)
        
        #add : add an element in set
        set1.add("Mukesh")
        print("Set after adding element Mukesh : " , set1)
        
        # remove a element from a set 
        set1.remove("Baalaji")
        print("Set after removing the Baalaji elemennt : " , set1)
        
        #union used to merge 2 set 
        set2={"A" , "K" , "s" , "H" , "a" , "Y" , "B",2,3,4}
        print(set2)
        
        set3=set1.union(set2)
        print("The union of set1 andd set2 is set3 : " , set3)
        
        #intersection common in set1 and set2 will be printed 
        set4=set1.intersection(set2)
        print("This is the set after the intersection of set1 and set2 : ",set4)
        print("The set1 after the intersection of the set2 " , set1)
        
        #intresection update will update the set1 with the intersection 
        set5=set1.intersection_update(set2)
        print("This is the set after the intersection update of set1 and set2 : ",set5)
        print("The set1 after the intersection_update is " , set1)
        
              
        set1={2,3,4,5,6,True,False , 0 ,1 ,23 , 34 , 45 , 56 , 67 ,78 , 89 ,10 ,"Akshaya" , "Baalaji" }
        set2={"A" , "K" , "s" , "H" , "a" , "Y" , "B",2,3,4}

        #difference Only the set without the element of set2 will be returned 
        print("Actual set is " , set1)
        set3=set1.difference(set2)
        print("The set differnce of set1 from set2  " , set3)

        #difference update : Only the set without the element of set2 will be returned and updated to set1 

        set4=set1.difference_update(set2)
        print("The set difference update after set1 and set2  " , set4)
        print("The set1 after difference update  " , set1)

        #symetric difference : leaves the intersection elements and print the distinct , unique element 
        set5 = set1.symmetric_difference(set2)
        print("The symetric differnce between set1 and set2 " ,set5)

        #symetric difference update  : leaves the intersection elements and print the distinct , unique element and update the result in set 
        set6 = set1.symmetric_difference_update(set2)
        print("The symetric differnce between set1 and set2 " ,set6)

        set1={2,3,4,5,6,True,False , 0 ,1 ,23 , 34 , 45 , 56 , 67 ,78 , 89 ,10 ,"Akshaya" , "Baalaji" }
        set2={"A" , "K" , "s" , "H" , "a" , "Y" , "B",2,3,4}

        #isdisjoint return whether same elements - false  No common elements true 

        print("Ths isdisjoint of set1 and set2  " , set1.isdisjoint(set2) )

        #issuperset :   set1 contains all elements of set2
        #issubset  :    set1 is completely contained within set2
        print("the subset of set1 and set2 is ", set1.issubset(set2))
        print("the superset of set1 and set2 is ", set1.issuperset(set2))


Exception handling :
    TYpe os exception :
        Zero division error 
        TypeError 
        
try 
    try is a place where we can expect exception happen 
    
    try must require either except , finally 
    
    Example :
        try :
            a=32/0
        except ZeroDivisionError as error :
            print("The error is ", err
                  
                 
except / finally
    is used for the handling the exception 
    
    What has to be done for the exception or error occured 
    
    Example :
        try :
            a=32/0
        except ZeroDivisionError as error :
            print("The error is ", err
else
    it is a place if everything goes right the code will be redirected to else part after the try block 
    
    if except occur else wont run 
    
    Ex :
        try :
            a=32/0
        except ZeroDivisionError as error :
            print("The error is ", error )
        else:  #this wont run because there is a error 
            print("No error")
        finally : # run at any stage even if error or no errir 
            print("Completed ")
            
            
finally 
    is is a place at any cost it will be running even error occur or not 
    
    Example :
        try :
            a=32/0
        except ZeroDivisionError as error :
            print("The error is ", error )
        else:  #this wont run because there is a error 
            print("No error")
        finally : # run at any stage even if error or no errir 
            print("Completed ")
          

Errors :
    Exception error :
        It is the common exception handler it can handle any type of error 
        
        Practical :
            #Zero exception error 
            try :
                a=99/0
            except Exception as e :
                print("The error arraises is :  " , e )

            #Type error 
            try:
                x = "hello" + 5  # This will raise a TypeError
            except TypeError as e :
                print("The error arraises is : " , e )

            #index error 
            try:
                fruits = ["apple", "banana", "cherry"]
                index = 5
                print("Fruit retrieved:", fruits[index])
            except IndexError as e :
                print("The error arraises is :  " , e )
                
            #HAndling the unexpected error using the exception 
            try:
                prunt
            except Exception as e:
                print("An unexpected error occurred:", e)

            #Keyerror 
            try:
                my_dict = {'a': 1, 'b': 2}
                value = my_dict['c']  # This will raise a KeyError
            except KeyError as e :
                print("The error arraises is  :  " , e )

            #Attribute error 
            try:
                x = 5
                x.append(10)  # This will raise an AttributeError
            except AttributeError as e :
                print("The error arraises is  :  " , e);

            #keyboard interrupt error 
            try:
                while True:
                    pass
            except KeyboardInterrupt as e :
                print("The error arraises is  :  " , e  )
                
        
"""












