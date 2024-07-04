country=[1,2,3,4,5,6]
satellite_count=[1,2,3,4,5,6]
launched_success=[1,2,3,4,5,6]
success_rate=[1,2,3,4,5,6]
for i in range (0,3,1):
    country[i]=input("Enter the country name ")
    satellite_count[i]=int(input("Total satellite count "))
    launched_success[i]=int(input("No of successfully launched satellite "))
    success_rate[i]=(launched_success[i]/satellite_count[i])*100
    print()
print("Printing Satellite details  ")
for i in range (0,3,1):
    print("{0} successfully launched {1} satellites and the success rate is {2}" .format(country[i],launched_success[i], int(success_rate[i])))

