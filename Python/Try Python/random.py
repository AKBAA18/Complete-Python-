import random
integer_num=random.randint(1,100)
print("Ramdom integer from 1 - 100 " , integer_num)
float_num=random.random()
print("Ramdom Float no argument needed " , float_num)
range_num=random.randrange(1,100)
print("Ramdom integer from 1 - 50 " , integer_num)
list_org=[1,2,3,4,5,6,7,8,9,10]
print("Original list  :" , list_org)
shiuffle_list=random.shuffle(list_org)
print("Original list shuffled  :" , list_org)
pick_any=random.choice(list_org)
print("Pick any fom the list : " , pick_any )

