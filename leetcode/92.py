# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        l = left
        ln = head
        while l-1 :
            ln = ln.next
            l -= 1

        r = right
        rn = head
        while r-1 :
            rn = rn.next
            r -= 1

        while left < right :
            ln.val , rn.val = rn.val,ln.val
            left += 1
            right -=1

        return head

    def display(self , head) :
        node = head
        while node :
            print(f"{node.val} -> ", end = "")
            node = node.next
        

if __name__ == "__main__" :

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    s = Solution()
    print("BEFORE : ")
    s.display(head)
    s.reverseBetween(head,1,4)
    # s.reverseBetween(head,2,4)
    # s.reverseBetween(head,1,3)

    print("\nAFTER : ")
    s.display(head)

    

