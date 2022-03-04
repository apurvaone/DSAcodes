   
def calc(arr,i,j,y,dp):
        
        
    if i>j:
        return 0
    
    if dp[i][j]!=-1:
        return dp[i][j]
    
    
        
        
    op1=arr[i] *y + calc(arr,i+1,j,y+1,dp)
    op2=arr[j]*y + calc(arr,i,j-1,y+1,dp)
        
    dp[i][j]=max( op1,op2  )
    return dp[i][j]
    
arr=[2,3,5,1,4]

i=0

dp=[[-1]*len(arr) for x in range(len(arr))]


x=calc(arr,0,len(arr)-1,1,dp)
print(x)
print(dp)
    
    
    
    
        
        