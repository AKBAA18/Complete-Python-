shop={"Caramel Ice Cream" : 30 , "Bubble Gum Ice Cream": 20 ,"Strawberry Ice Cream": 10 ,"Cookies and Cream" : 30}
print("*****************Menu is***********************")
for key, value  in shop.items(): 
     print(key , end=" " )
     print("Rs " , value )
print("Enter your order ")
caramel_icecream=0
bubblegum_icecream=0
strawberry_icecream=0
cookies_icecream=0
def order():
    global caramel_icecream, bubblegum_icecream,strawberry_icecream,cookies_icecream
    caramel_icecream=int(input("Enter the number of caramel icecream "))
    bubblegum_icecream=int(input("Enter the number of Bubble gum ice cream "))
    strawberry_icecream=int(input("Enter the number of Strawberry ice cream "))
    cookies_icecream=int(input("Enter the number of Cookies and cream "))
order()
print()
print()
for key, value  in shop.items(): 
     print(key)
     print("Total Amount " , value )
     count=0
     if key is 'Caramel Ice Cream':
         print("Quantity is " , caramel_icecream)
         print("Cost :" , value*caramel_icecream)
     if key is 'Bubble Gum Ice Cream':
         print("Quantity is " , bubblegum_icecream)
         print("Cost :" , value*bubblegum_icecream)
     if key is 'Strawberry Ice Cream':
         print("Quantity is " , strawberry_icecream)
         print("Cost :" , value*strawberry_icecream)
     if key is 'Cookies and Cream':
         print("Quantity is " , cookies_icecream)
         print("Cost :" , value*cookies_icecream)
print("Bye")
     
    