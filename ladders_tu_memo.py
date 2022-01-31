def fun(n,k):
    
    if n==0 :
        return 1
    
    if n<0:
        return 0
    
   
    r=0   
    for i in range(1,k+1):
        
        
            
        r+= fun(n-i,k)
            
            
    return r
    
    
    
print(fun(7,3))
    
    
    
    

    
    
            
            
            
        