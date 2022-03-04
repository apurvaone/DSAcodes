
def calc(arr,n,dp):
    
    for i in range(n-1,-1,-1):
        for j in range(0,n):
            if i<=j:
                if i==j:
                    
                    dp[i][j]= n* arr[i]
                    
                else:
                    
                    y= n- (j-i)   
                    
                    l= y* arr[i] + dp[i+1][j]
                    r= y* arr[j]+ dp[i][j-1]
                    
                    dp[i][j]= max(l,r)
                    
    
    
    return dp[0][n-1]



arr=[2,3,5,1,4]

i=0

dp=[[0]*len(arr) for x in range(len(arr))]

x= calc(arr,5,dp)

print(x)
                    
                
                
            
            

    
    