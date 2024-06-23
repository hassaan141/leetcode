// Definition for singly-linked list.
// struct ListNode {
// int val;
// ListNode *next;
// ListNode() : val(0), next(nullptr) {}
// ListNode(int x) : val(x), next(nullptr) {}
// ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode* list3= new ListNode();
        tail = list3;

        while (list1->next && list2->next != nullptr){
            if (list1->val>list2->val){
                list3->val = list1->val;
                list1 = list1->next
                list3 = list3->next;
            }
            else if (list1->val == list2->val){
                list3->val = list1->val;
                list3 = list3->next;
                list1 = list1->next;
                list3->val = list2->val;
                list3 = list3->next;
                list2 = list2->next;
            }
            else{
                list3->val = list2->val;
                list2 = list2->next;
                list3 = list3->next;
            }
        }

        if (list1 && list2 == nullptr)
        {
            return list3;

        }
        else if (list1!= nullptr){

        }
    }
}