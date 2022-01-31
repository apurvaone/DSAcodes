def ways(n,k):
    
    
    if n==0:
        return 1
    
    d=[0] * (n+1)
    
    d[0]=1
    
    for i in range(1,n+1):
        
        
        
        if i-k>=0:
            
            d[i]= d[i-1]+ d[i-1] -d[i-1-k]
            
        else:
        
            j= i-1
            c=0
        
            while j>=0 and c<k :
            
                d[i]+=d[j]
                c+=1
                j-=1
            
    return d[n]


print(ways(4,3))