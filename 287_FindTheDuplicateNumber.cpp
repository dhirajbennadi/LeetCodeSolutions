class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        map<int,int> mp;
        int retVal = 0;
        
        for(int i = 0; i < nums.size(); i++)
        {
            mp[nums[i]] += 1;
            if(mp[nums[i]] == 2)
            {
                retVal = nums[i];
            }
        }
        
        return retVal;
        
    }
};