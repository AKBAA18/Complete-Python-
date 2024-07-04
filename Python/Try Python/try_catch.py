"""
try :
    a=45/0
except ZeroDivisionError as error :
    print(error)
"""
try :
    if True :
        print("Hi")
except IndentationError as error :
    print("This error is " , error )

else : 
    print("No errors ")

finally :
    print("Compleyted")