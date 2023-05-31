def Print (_i, _j): 
    print(_i, "+", _j) 
     
nums = [1, 4, 3, 6, 9, 7] 
 
for i in nums: 
    for j in nums: 
        if i + j == 10: 
            print(i,j)