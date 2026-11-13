arr = [10, 20, 10, 30, 40, 20, 50, 30, 60]

def sec_larg_ele(arr):
    max_ele = arr[0]
    sec_larg = arr[0]

    for i in range(1,len(arr)):
        if(arr[i]>max_ele):
            sec_larg = max_ele
            max_ele = arr[i]
        
        elif(arr[i]<max_ele and arr[i]>sec_larg):
            sec_larg = arr[i]

    return sec_larg
    
sec_max = sec_larg_ele(arr)
print(sec_max)
