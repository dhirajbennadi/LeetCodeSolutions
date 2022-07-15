class Solution {
public:
    bool isAnagram(string s, string t) {
        
        map<char, int> string1;
        map<char, int> string2;
        
        for(int i = 0; i < s.size(); i++)
        {
            string1[s.at(i)] += 1;
        }
        
        for(int i = 0; i < t.size(); i++)
        {
            string2[t.at(i)] += 1;
        }
        
        if(string1 == string2)
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }
};