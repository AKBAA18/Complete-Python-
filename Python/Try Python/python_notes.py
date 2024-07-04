# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 09:31:03 2024

@author: aksha
"""

#multi line value :
strings=""" HI 
Hello 
Goodbye """
print(strings)

"""
INTERPRETER :
    It eveluates line by line 
    if there is a error in a function 
        it wont be found out till the funciton is called 
        
COMPILER :
    It eveluates all the lines at once 
    if there is a error in a function 
        it sill show it even the funciton is not called 
    
"""
"""
Python is a dynamic inference language -(Which identifies its own variable datatype )

Python is a strongly typed programming language 
#the below prog shows that it automatically finds a as int 
    a=12
    strings="Hi BYe"
    print(strings + a);

"""

"""
variable :
   Formal Def : A name or identifier to refer the memory location of a object or variable 
    not strt  with special charecter except _ 
    variable must contain alphanumeric charecters and underscore 
    Variable are case sensitive 
    Multi assignment : multiple varible assigned on single line 
        ex a,b,c =1,2,3
            a,b,c=1,2,3
            print(a)
            print(b)
            print(c)

Type Casting :
    Changing the datatype of the variable 
    The originality of the variable wont be changed in type casting     
        a=1;
        aa=(str)a;
        string1="Hi BYe "
        print(string1+aa) # there will be no error 
    FUncitons:
        int , float , str , list , tuple , dict , set  
        Ex :
            number=1000
            string_num = str(number)
            float_num=float(number)
            #char_number=char(number)
            list_number=list(string_num)
            tuple_number=tuple(string_num)
            set_number = set(string_num)
            #dictionary_number=dict(number )


            print(string_num)
            print(float_num)
            print(list_number)
            print(tuple_number)
            print(set_number)
    #this will be string by default 
    number=input("Enter a String or NUmber ")
    print(type(number))
    #so type cast 
    number1=int(input("Enter the number because it is type casted at time of input itself "))
    print(type(number1))
    
Constrains :
If is for Checking    :
    if isinstance(variable,datatype):
        #print("The isinstance checks the variable is string or not ")
        ex :
            aa=str(a)
            print(strings + aa);
            #isinstance usage 
            if isinstance (aa,str):
                print("It is a string daatype")

Ternary operator :
    Ex :
        n=input("Enter the input ")
        add=10
        summ=add+n if isinstance (n, int) else int(n)+add
        print("Your addition is " , summ)
        
Functions :
    Functions are mainlly used ofr the reusability 
    Ex :
        def add (a,b)://a and b are arguments 
            return a+b;// we are ending the function by the return 
        
Format function :
    1 st way 
        #format example 1 (Hardcoring a variable )
        strings="ENter your name {name} and your age {age}".format(name="Akshay" , age=34)
        print(strings)
    
        #format example 2 (psasing the parameter as the prev variables )
        fname="Akshaya Baalaji"
        page=21
        strings="Hi {name} and your age {age}".format(name=fname , age=page)
        print(strings)
    2 nd way 
        age=12
        fname="Akshaya baalaji"
        strings=f"Hi {0} your age is {0}"

        print(strings)

String :
#string is a iterable type and 
#it is a collection of charecter in sequence 
  Mutable and Immutable : If a variable value can be changed it is mutable and if not immutabble 
      list =[1,2,"Akshaya"]
      list[2] = "Baalaji"
      #the above can be done because list , set , dictionary are mutable 
      strings="Akshaya Baalaji"
      strings[0]='A'
      #this is not possible because string is immutable 

Static inference :
    name="Akshaya Baalaji "
Dynamic inference :
    name :str="Akshaya Baalaji "
    #this is for the definition that name is a variable will be of type string 
        Even if you enter the integer in it it can identify it because of the dynamic infernce in python 
        Ex:
            number:str=9
            print(type(number)) // type int
          
            
Numeric : 
    int 
        ex: 
            int_prac=234
    float 
        ex: 
            float_prac=123.32432
    complex 
        ex : 
            complexx = 100e100
            exponent_prac= 100e2 // 10000.0



Convert a variable value to binary :
    Ex:
        salary=12323
        bin_bytes=bytes(salary)


Operators :

Assignment operator :
    used to assign the value to variable 
    usually = (or) operator =
    (+ , - , * , / , ** , ^)

Relational / comparision operator :
    (== , >= , <= , != , >  , < )
    return the boolean result 

Logical operator :
    Return only boolean value 
    and , or , not 
    
    Ex :
        #or 
        a =10
        if ((a==10) or (a==11)):
            print("The a is 10 or a is 11 ")
        else :
            print("a is not either 10 or 11 ")
        
        #and
        a=10
        if ((a==10) and (a%2==0)):
            print("The a is 10 and the divisible of 2  ")
        else :
            print("a is not either 10 or divisible of 2 ")
            
Bitwise operator :
    same like logical operator 
    costly to use because it does the comparision bit by bit returning the true or false
    & , | , ^ , ~  same as logical operator 
    
    
Ternary opreator :
    Ex :
        mark=232
        total_mark=400
        internal=100
        consolidate=mark+internal if(mark >200) else mark
    

Built in funcitons :
    Understand the function by doing the hower on that function 
    
    1. split in string 
    Ex :
        string="i am Akshaya Baalaji i am from thanjavur "
        
        list_of_str=list(string)
        print(list_of_str)
        string_spli=list(string.split(" "));
        print(string_spli)
        string_spli=list(string.split(" " ,2));# 2 is the index till we need to split 
        #on above the split will be done for the first 2 index and make the remaining content in 3third index 

        
    2. capitalize : make the first letter as capital 
    Ex:
        print(string.capitalize()) 
        
    3. upper , lower #make all charecter ass upper / lower 
    Ex :
        print(string.upper())
        print(string.lower())

    4. title #make all start charecter as upper case 
    Ex :
        print(string.title())

    5.format (important ) 
    Ex:
        string_new="I am {3} and I am from {2} and I am specialized in {1} and my age is {0}"
        print(string_new.format(21,"Bigdata","TNJ","Akshaya Baalaji"))
 
    6. replace 
    Ex :
        print(string.replace("Akshaya", "AAkshaya"));
        #the above function replace all the occurence of the string 
        print(string.replace("A", "X",2));
        #the above function represent the number of times we need to apply the replace on the string 
        
    7.count #count the number od occurence of the find 
    Ex :
        print(string.count("A")); # do a full search on the string to find the number of occurences 
        print(string.count("A",0,9));
        #the above count we are mentioning the index where to start and end the count of occurence 

    8.strip and rstrip 
    Ex :
        print("Strip....................")
        print(" a b c d    ".strip()) # remove leading and trailing white spaces 
        print("      a b  c  d    ".rstrip()) # remove the spaces at the end 

    9._ _lt_ _ # return boolean and it is less than 
    Ex :
        a=10
        print(a.__lt__(11)) #true 
        
    10. We can also import funcitons from the modules 
    Ex :
        import math # module from which we are going to use function 
        floatvar=100.34
        print(floatvar.__floor__()) 
        #usually the floor cant be applied on the float and will only be applied on the int 
        #so we are using the float funciton from the math module for solving it 

COnditional structure or control flow :
    These are the case conditional structure which control the flow of the program 
    1. if : 
        there can be only one if without else - true 
        there can be only one else and elif without if - false 
        possible conditional structure in if :
            1.if 
            2.if else 
            3. if elif else 
            Ex :
                inputt=int(input("Enter a number "))
                if(inputt==0):
                    print("Zero")
                if(inputt==1):
                    print("One")
                if(inputt==2):
                    print("Two")
                if(inputt==3):
                    print("Three")
                    
                using elif :
                    inputt=int(input("Enter a number "))
                    if(inputt==0):
                        print("Zero")
                    elif(inputt==1):
                        print("One")
                    elif(inputt==2):
                        print("Two")
                    elif(inputt==3):
                        print("Three")
                    else :
                        print("SOme other numbers ")
            
            2. pass : #used for passing / skipping the current iteration 
            Ex : 
                if(a==1):
                    print("1")
                else :
                    pass #skip the iteration 
                   


Practical :
    1. greater of three number 
    Code :
        a=10
        b=10
        c=30
        if a>=b and a>=c :
            print(a, " is greater ")
        elif b>=a and b>=c :
            print(b, " is greater ")
        else :
            print(c, " is greater ")
    
    2. 

Practical Irfan exercise :
    #using list built in functions 
    make_list=[a,b,c] # making the list from the variables 
    print(max(make_list));
    #we can take the greatest by sorting and taking the last element in list 
    make_list.sort(); #sort will sort the list 
    print("Taking the last elemrent from the list ",make_list[-1])

n
    #using simple conditional structure 
    a=10
    c=10
    b=30
    if a==b and a==c :
        print("All are same ")
    elif a>=b and a>=c :
        print(a, " is the greatest ")
    elif b>=a and b>=c :
        print(b, " is the greatest ")
    else :
        print(c, " is the greatest ")

    
    #using nested conditional structure 
    a=10
    b=10
    c=30

    if a==b and b!=c:
        if a>=b and a>=c :
            print(a , " is the greatest ")
        elif b>=a and b>=c :
            print(b," is the greatest ")
        else :
            print(c , " is the greatest ")
    else :
        print("All are same ")

"""
#variable properties 
#Dynamic inference
