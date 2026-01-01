def merge(left,right):
    result=[]
    i=j=0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort(arr):
    step=1
    length=len(arr)
    
    while step<length:
        for i in range(0,length,2*step):
            left=arr[i:i+step]
            right=arr[i+step:i+2*step]
            
            merged=merge(left,right)
            
            for j,val in enumerate(merged):
                arr[i+j]=val
                
        step*=2
    return arr
        
        