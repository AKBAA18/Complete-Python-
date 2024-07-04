# we have use thre reduce from the functools 
#reduce if a function to reduce a list to a single value
from functools import reduce 
list_1=[1,2,3,4,5,6,7,8,9,10]
reduce_val=reduce(lambda x,y: x+y , list_1 )
print(reduce_val)