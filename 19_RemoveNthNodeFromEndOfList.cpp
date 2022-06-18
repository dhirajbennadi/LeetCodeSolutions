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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = head;
        int count = 0;
        
        while(temp != NULL)
        {
            temp = temp->next;
            count++;
        }
        
        //cout << count << endl;
        int nodeToBeRemoved = count - n;
        
        if(nodeToBeRemoved < 0)
        {
            head = NULL;
            return head;
        }
        else if(nodeToBeRemoved == 0)
        {
            head = head->next;
            return head;
        }
        
        temp = head;
        ListNode *dummy;
        
        while(nodeToBeRemoved)
        {
            dummy = temp;
            temp = temp->next;
            nodeToBeRemoved--;
            
        }
        
        if(dummy != NULL)
        {
            dummy->next = temp->next;
        }
        
        return head;
    }
};