"""
Bigdata Function 
Just a program to increment a number by a function rather than doing a low level coding 

def funciton_sequence (a):
    print()
    while True : 
        print(a , end=" ")
        if a==20 :
            break
        a=a+1
var=12
funciton_sequence(var)
var_1=1
funciton_sequence(var_1)

Funciton are composible 

a="Akshaya Baalaji"
b= a.lower().index('b') # passing the output of the lower to index function 
print(a)
print(b) 
"""
#funcitons are not time bounded 
#the below code is time oriented 
a=1
if a>=1 :
    a=a+1
print(a)
# when we put the above code in a function it become non time bounded 
a=1
def function ():
    global a 
    if a>=1 :
        a=a+1
    print(a)        
function()
