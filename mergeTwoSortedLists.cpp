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
        ListNode* p1 = head1; // pointer (to a node)
        ListNode* p2 = head2; // pointer (to a node)
        ListNode* dummyNode = new ListNode(-1); // a new node
        ListNode* p3 = dummyNode;

        while (p1 != NULL && p2 != NULL) {
            if (p1->val < p2->val) {
                p3->next = p1;
                p1 = p1->next;
            } else {
                p3->next = p2;
                p2 = p2->next;
            }
            p3 = p3->next;
        }
        
        while(p1 != NULL) {
            p3->next = p1;
            p1 = p1->next;
            p3 = p3->next;
        }

        while(p2 != NULL) {
            p3->next = p2;
            p2 = p2->next;
            p3 = p3->next;
        }

        return dummyNode->next;

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