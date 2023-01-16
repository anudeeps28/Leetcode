#include<iostream>
using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    // this function will return the head of the 2 merged linked lists
    ListNode* mergeTwoLists(ListNode* head1, ListNode* head2) { // takes as input the heads of linked lists
        if (head1 == NULL) return head2;
        if (head2 == NULL) return head1;

        if(head1->val>=head2->val) head2->next = mergeTwoLists(head1, head2-> next);
        else{
            head1->next = mergeTwoLists(head1->next, head2);
            head2 = head1;
        }return head2;

    }
};

int main () {

    Solution S;

    ListNode l1_1(1);
    ListNode l1_2(2);
    ListNode l1_3(4);
    l1_1.next = &l1_2;
    l1_2.next = &l1_3;

    ListNode l2_1(1);
    ListNode l2_2(3);
    ListNode l2_3(4);
    l2_1.next = &l2_2;
    l2_2.next = &l2_3;
    
    S.mergeTwoLists(&l1_1, &l2_1);

    return 0;
}