def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid=len(arr)//2
    leftHalf=arr[:mid]
    rightHalf=arr[mid:]
    
    sortLeft=mergeSort(leftHalf)
    sortRight=mergeSort(rightHalf)
    
    return merge(sortLeft,sortRight)

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

arr=[8,9,2,3,1]
print(mergeSort(arr))