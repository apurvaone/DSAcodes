def knapsack_bu(prices,weight,N,W):
    
    dp=[[-1]* (W+1) for x in range(N+1)]
    
    for n in range(1,N+1):
        
        for w in range(1,W+1):
            
            inc=0
            exc=0
            if weight[n-1]<=w:
                
                inc= prices[n-1]+ dp[n-1][w-weight[n-1]]
                
            exc= dp[n-1][w]
            
            dp[n][w]= max(inc,exc)
            
    
    return dp[N][W]


x= knapsack_bu([5,20,20,10],[2,7,3,4],4,11)
print(x)
            
                
            
    
    
    
    
    
    
    
    
    
    

    
    