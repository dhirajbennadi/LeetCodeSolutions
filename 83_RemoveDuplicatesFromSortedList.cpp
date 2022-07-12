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
    ListNode* deleteDuplicates(ListNode* head) {
        
        if(head == NULL)
        {
            return NULL;
        }
        map<int,int> mp;
        
        ListNode *temp = head;
        
        while(temp != NULL)
        {
            mp[temp->val] += 1;
            temp = temp->next;
        }
        
        ListNode *result = new ListNode();
        ListNode *headNode = result;
        
        for (const auto &item : mp) 
        {
            if(item.second > 0)
            {
                //ListNode *dummyObj = new ListNode(item.first);
                //result->next = dummyObj;
                //ListNode dummyObj(item.first);
                //cout << dummyObj.val << endl;
                //cout << item.first << endl;
                //ListNode *dummyObj = new ListNode(item.first);
                result->next = new ListNode(item.first);
                result = result->next;
            }
        }
        
        return headNode->next;
        //return head;
        
    }
};