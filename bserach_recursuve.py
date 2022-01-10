def bsearch_rec(arr,l,r,el):
    
    
    if l>r:
        return -1

    mid= (l+r)//2
    
    if arr[mid]==el:
        return mid
    
    elif arr[mid]<el:
        return bsearch_rec(arr,mid+1,r,el)
        
    else:
        return bsearch_rec(arr,l,mid-1,el)
        
        p= bsearch_rec([1,2,3,4,8,6,9],0,6,7)

print(p)
    
    
     