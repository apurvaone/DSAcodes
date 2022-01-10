
def binary_search(input_array, value):
    """Your code goes here."""
    
    l=0
    r= len(input_array)-1
    
    while l<=r:
        
        mid= (l+r)//2
        
        if value==input_array[mid]:
            return mid
        
        elif value>input_array[mid]:
            l=mid+1
            
        else:
            r= mid-1
            
    return -1
    
    
    
    

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print( binary_search(test_list, test_val1) )
print( binary_search(test_list, test_val2) )