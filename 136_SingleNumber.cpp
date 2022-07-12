class Solution {
public:
    int singleNumber(vector<int>& nums) {
    int retVal = 0;
    
    for(int i = 0; i < nums.size(); i++)
    {
        retVal ^= nums[i];
    }
    
    return retVal;
    }
};