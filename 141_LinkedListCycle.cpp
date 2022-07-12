/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        
        if(head == NULL)
        {
            return false;
        }
        #if 0
        ListNode *temp = head;
        ListNode *check;
        int count = 0;
        
        map<int, int> a;
        
        while(1)
        {
            check = temp->next;
            
            //cout << check->val << endl;
            
            if(check != NULL)
            {
                if(a.find(check->val) == a.end())
                {
                    a[count] = temp->val;
                    count++;
                }
                else
                {
                    return true;
                }
            }
            else
            {
                return false;
            }
            
            temp = temp->next;
            
        }
        #endif
        
        
        ListNode *slow = head;
        ListNode *fast = head;
        
        while(fast->next && fast->next->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            
            if(slow == fast)
            {
                return true;
            }
        }
        
        return false;
        
    }
};