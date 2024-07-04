#error handling :
while True:
    try :
        i=int(input("Enter a numebr "))
        print("THe number is " , i )
        i=i+spam #NameError
        i='2'+i #TypeError
        print("THe number is " , i )
    except ValueError:
        print("This is the error caused by the wrong entering of input")
    except NameError:
        print("You have used the undeclared variable ")
    except TypeError:
        print("You have entered sonmething wrong there ")
        break

    