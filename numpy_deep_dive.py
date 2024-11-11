## Here , we are going to apply some of our concepts till what've we learnt right now. 

import numpy as np 

## Linspace 

arr_1 = np.linspace(10,100,10)
arr_1.resize(2,5)
# print(arr_1)

arr_2 = np.arange(10)
arr_2.resize(2,5)
# print(arr_2)

arr_sum = arr_1 + arr_2
# print(arr_sum)

## Stacking this name-char into the arr by converts it into ascii values. 
crush_name = "seolina"
name_list = list(crush_name)

for i in range(len(name_list)):
    
    if (i<5) :  
        arr_1[0,i] = ord(name_list[i]) ## ord() method used to convert the chars into the integral values. 
        

    elif (i == 5): 
        arr_1[1,0] = ord(name_list[i])
        
    elif (i == 6): 
        arr_1[1,1] = ord(name_list[i])
        
    else : 
        break

print(arr_1)


print(f"The total byte size of the arr         is : {arr_1.itemsize * arr_1.size}")


## Here , we are going to do some questions on numpy array . 


"""

// Questions 
How to create an empty and a full NumPy array?
Create a Numpy array filled with all zeros
Create a Numpy array filled with all ones
Check whether a Numpy array contains a specified row
How to Remove rows in Numpy array that contains non-numeric values?
Remove single-dimensional entries from the shape of an array
Find the number of occurrences of a sequence in a NumPy array
"""

## Numpy array

# 1. 
# empty_arr = np.empty(2,2)
# full_arr = np.full_like(2,3)
# print(full_arr)


#2. zeros arr 
zero_arr = np.zeros(2)
# print(zero_arr)

one_arr = np.ones(2)
# print(one_arr)


arr_num = np.array([23,44,32,21] , [25,65,87,34])
print(arr_num)

