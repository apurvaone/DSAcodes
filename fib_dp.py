def fib(num):
    
    dp= [0] * (num +1)
   
    
    if num==0 or num==1:
        return num
    
    dp[0]=0
    dp[1]=1
    
    for i in range(2,num+1):
        
        dp[i]= int(dp[i-1] )+ int (dp[i-2])
        
    return dp[num]


print(fib(100))