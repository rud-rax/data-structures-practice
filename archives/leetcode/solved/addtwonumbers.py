# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        al = None
        c = 0

        while l1 or l2:

            no = 0
            if not al:
                al = ListNode()
                head = al
            else:
                al.next = ListNode()
                al = al.next

                if c:
                    no = c
                    c = 0

            if l1:
                no += l1.val
                l1 = l1.next

            if l2:
                no += l2.val
                l2 = l2.next

            if no >= 10:
                c = 1
                no = no % 10

            al.val = no
            # print(al.val)

        if c:
            al.next = ListNode(1)

        return head


if __name__ == "__main__":

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    ll1 = None
    ll2 = None

    for i in l1[::-1]:
        i = ListNode(i, ll1)
        ll1 = i

    for i in l2[::-1]:
        i = ListNode(i, ll2)
        ll2 = i

    s = Solution()

    al = s.addTwoNumbers(ll1, ll2)

    while al:
        print(al.val)
        al = al.next
