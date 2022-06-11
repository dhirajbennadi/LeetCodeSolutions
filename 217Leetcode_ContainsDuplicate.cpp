class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        map<int,int> mp;
        
        for(int i = 0; i < nums.size(); i++)
        {
            mp[nums[i]] += 1;
        }
        
        for(auto x:mp)
        {
            //cout << x.first << " " << x.second << endl;
            if(x.second > 1)
            {
                return true;
            }
        }
        
        return false;
    }
};