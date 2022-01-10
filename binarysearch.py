def bsearch(arr,el,l,r):
    

    
    while l<=r:
        
    
    
        mid= (l+ r) //2
        
        print(mid)
        
        
        if el == arr[mid]:
            return mid
        
        elif el>arr[mid]:
            
            l= mid+1
                
        else:
            
            r= mid-1
            
    
    return -1


p= bsearch([1,2,3,4,5,6,7],7,0,6)
print(p)
        
        
        
    