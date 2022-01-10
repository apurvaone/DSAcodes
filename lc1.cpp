class Solution {
public:
    int reverse(int x) 
    {
       int flag=0;
        
        if(x<0)
        {
            x= -x;
            flag=1;
        }
        
        int rev= 0, prev_rev=0;
        while((x)>0)
        {
           
              // if(rev*10!= rev/10|| rev*10+10> 2147483647)
              //   return 0;
            
           rev= rev* 10+ x%10;
            
            if((rev-10)/10!= prev_rev)
                return 0;
            
            prev_rev = rev;
            
            x= x/10;
            
           
            
        }
        
        if(flag==1)
            return (-rev);
        else
        {
        return rev;
        }        
        
    }
};