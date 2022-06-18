class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> mp;
        
        for(int i = 0; i < nums.size(); i++)
        {
            mp[nums[i]] += 1;
        }
        
        
        vector<int> tempVector;
        vector<int> resultVector = {};
        
        for(auto x:mp)
        {
            //cout << x.first << " " << x.second << endl;
            tempVector.push_back(x.second);
        }
        sort(tempVector.begin(), tempVector.end(), greater<int>());
        
        // for(int i = 0; i < tempVector.size(); i++)
        // {
        //     cout << tempVector[i] << " ";
        // }
        // cout << endl;
        
        
        for(int i = 0; i < k; i++)
        {
            for(auto x:mp)
            {
                if(x.second == tempVector[i])
                {
                    resultVector.push_back(x.first);
                    mp.erase(x.first);
                    break;
                }
            }
            
        }
    
        // for(int i = 0; i < resultVector.size(); i++)
        // {
        //     cout << resultVector[i] << " ";
        // }
        return resultVector;
        
        
    }
};