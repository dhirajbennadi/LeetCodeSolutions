class Solution {
public:
    int hammingWeight(uint32_t n) {
    int i;
    int count = 0;
    int temp = 0;
    
    for(i = 0; i < 32; i++)
    {
        temp = n & (1 << i);
        
        if(temp)
        {
            count++;
        }
        
    }
    
    return count;
        
    }
};