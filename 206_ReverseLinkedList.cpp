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
    ListNode* reverseList(ListNode* head) {
        
        ListNode *prev;
        ListNode *current;
        ListNode *next;
        
        prev = NULL;
        current = next = head;
        
        while(next != NULL)
        {
            next = next->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        
        head = prev;
        
        return head;
        
    }
};