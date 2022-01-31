from tkinter import N


def fib(n,dp):
    
    if n==0 or n==1:
        return n
    
    if dp[n]!=-1:
        return dp[n]
    
    dp[n] = fib(n-1,dp) + fib(n-2,dp)
    
    return dp[n]
    



print(fib(100,[-1]* 101))
    
     
    
    