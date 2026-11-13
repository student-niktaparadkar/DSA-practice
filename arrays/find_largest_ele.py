arr = [10, 20, 10, 30, 40, 20, 50, 30, 60]

def largest_ele(arr):
    ele = arr[0]

    for i in range(1,len(arr)):
       if(ele<arr[i]):
           ele = arr[i]
    
    return ele      

max_ele = largest_ele(arr)
print(max_ele)
