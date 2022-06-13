class Solution {
public:
    int missingNumber(vector<int>& nums) {
//         int value = 0;
//         vector<int>::iterator it;
        
//         for(int i = 0; i <= nums.size(); i++)
//         {
//             it = find(nums.begin(), nums.end(), i);
//             if(it == nums.end())
//             {
//                 value = i;
//             }
//         }
        
//         //cout << value << endl;
        
//         return value;
        
        int xorValue = 0;
        
        for(int i = 0; i < nums.size(); i++)
        {
            xorValue ^= nums[i] ^ i;
        }
        
        xorValue ^= nums.size();
        
        return xorValue;
    }
};