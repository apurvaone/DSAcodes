def knapsack(n,w,prices,weight,dp):
    
    if n<=0 or w<=0:
        return 0
    
    if dp[n][w]!=-1:
        return dp[n][w]
    
    inc=0
    exc=0
    if w-weight[n-1]>=0:
        
        inc= prices[n-1]+ knapsack(n-1,w-weight[n-1],prices,weight,dp)
    exc = knapsack(n-1,w,prices,weight,dp)
        
    dp[n][w]= max(inc,exc)
    return dp[n][w]

weight=[2,7,3,4]
n=11


dp= [[-1]* 12 for x in range(5)]

x= knapsack(3,11,[5,20,20,10],[2,7,3,4],dp)

print(dp)

print(x)
    
    
    