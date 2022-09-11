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
    ListNode* insertionSortList(ListNode* head) {
        
        vector<int> toSort;
        
        ListNode *temp = head;
        
        while(temp)
        {
            toSort.push_back(temp->val);
            temp = temp->next;
        }
        
        
        /*Use Insertion Sort to Sort the Numbers*/
        sort(toSort.begin(), toSort.end());
        
        ListNode *dummy = new ListNode();
        
        ListNode *temp2 = dummy;
        
        for(int i = 0; i < toSort.size(); i++)
        {
            temp2->next = new ListNode(toSort.at(i));
            temp2 = temp2->next;
        }
        
        return dummy->next;
            
        
    }
};