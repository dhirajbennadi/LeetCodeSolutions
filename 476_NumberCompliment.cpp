class Solution {
public:
    int findComplement(int num) {
        
        int count = 0;
        int newNum = 0;
        int temp = num;
        
        while (temp)
        {
            temp = temp / 2;
            count++;
        }
        
        //cout << "Count = " << count << endl;
        unsigned int val = 0;
        
        for(int i = 0; i < count; i++)
        {
            val = (num >> i) & 0x01;
            val = val ^ 1;
            newNum = newNum | (val << i);
        }
        
        return newNum;
    }
};