def fun(n,k):
    
    if n==0 :
        return 1
    
    
    
    if n-k>=0:
        
        r=0
        
        for i in range(1,k+1):
            
            r+= fun(n-i,k)
            
            
        return r
    
    
    else:
        
        j=n-1
        
        r=0
        c=0
        
        while c<k and j>=0:
            
            r+= fun(j,k)
            j-=1
            c+=1
            
        return r
    
    
    
    
print(fun(6,3));
    
    

    
    
            
            
            
        
        
    
    
    
    
    
    
        
        
        