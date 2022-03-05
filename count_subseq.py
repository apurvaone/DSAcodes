

def count(i,j,s,t):
    
    
    if (i==-1 and j==-1) or (j==-1):
        return 1
    
    if i==-1:
        return 0
    
    
    if s[i]==t[j]:
        
        return (count(i-1,j,s,t) + count(i-1,j-1,s,t))
    
    
    else:
        return (count(i-1,j,s,t))
    
    

x= count(5,2,'abcdce','abc')

print(x)