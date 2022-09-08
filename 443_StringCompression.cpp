class Solution {
public:
    int compress(vector<char>& chars) {
        
        
        vector<char> dummy;
        int count = 1;
        char current;
        char prev;
        dummy.push_back(chars.at(0));
            
        for(int i = 1; i < chars.size(); i++)
        {
            current = chars.at(i);
            prev = chars.at(i-1);
            
            if(current == prev)
            {
                count++;
            }
            else
            {
                if(count > 1)
                {
                    if(count > 9)
                    {
                        int number = count;
                        vector<int> numberList;
                        
                        while(number)
                        {
                            numberList.push_back(number % 10);
                            number = number / 10;
                        }
                        
                        //numberList.reverse();
                        reverse(numberList.begin(), numberList.end());
                        
                        for(int j = 0; j < numberList.size(); j++)
                        {
                            dummy.push_back('0' + numberList.at(j));
                        }
                        count = 1;
                        
                    }
                    else
                    {
                        dummy.push_back('0' + count);
                        count = 1;
                    }
                }
                dummy.push_back(current);
            }
        }
        
        if(count > 1)
        {
            if(count > 9)
            {
                        int number = count;
                        vector<int> numberList;
                        
                        while(number)
                        {
                            numberList.push_back(number % 10);
                            number = number / 10;
                        }
                        
                        //numberList.reverse();
                        reverse(numberList.begin(), numberList.end());
                        
                        for(int j = 0; j < numberList.size(); j++)
                        {
                            dummy.push_back('0' + numberList.at(j));
                        }
                
            }
            else
            {
                dummy.push_back('0' + count);
                count = 1;
            }
        }
        
        for(int i = 0; i < dummy.size(); i++)
        { 
            chars.at(i) = dummy.at(i);
        }
        
        return dummy.size();
        
        
    }
};