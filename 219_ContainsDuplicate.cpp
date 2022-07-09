class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int , int> mp;
        int current = 0;
        
        for(int i = 0; i < nums.size(); i++)
        {
            current = nums[i];
            if(mp.find(current) != mp.end() && (i - mp[current]) <= k)
            {
                return true;
            }
            else
            {
                mp[current] = i;
            }
        }
        
        return false;
        
    }
};