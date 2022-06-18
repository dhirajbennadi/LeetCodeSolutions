/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        
        ListNode *temp = head;
        vector<int> result;
        
        while(temp != nullptr)
        {
            result.push_back(temp->val);
            temp = temp->next;
        }
        
        int left = 0;
        int right = result.size() - 1;
        
        temp = head;
        
        while(left <= right)
        {
            temp->val = result[left];
            if(left != right)
            {
                temp->next->val = result[right];
                temp = temp->next->next;
            }

            left += 1;
            right -= 1;
        }
    }
};