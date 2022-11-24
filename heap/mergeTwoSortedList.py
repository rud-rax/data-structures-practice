import heapq
import math

class Node() :
    def __init__(self , val = math.inf , next = None) :
        self.val = val
        self.next = next

    # def __lt__(self,node ) :
    #     return self.val < node.val


class LinkedList() :
    def __init__(self, head = None) :
        self.head = head
    def addNode(self , val) :
        if not self.head :
            self.head = Node(val)
            return
        
        node = self.head
        while node.next :
            node = node.next

        node.next = Node(val)

    


if __name__ == "__main__" :

    list1 = [1,2,4]
    list2 = [1,3,4]

    ll1 = LinkedList()
    ll2 = LinkedList()

    
    for i in list1 :
        ll1.addNode(i)
        # print(i , end = " ")

    # print(ll1)
    # print("________________")
    print()
    for i in list2 : 
        ll2.addNode(i)
        # print(i , end = " ")


    # print(ll2)
    # print("________________")

    ll1 = ll1.head
    ll2 = ll2.head
    hp = []
    heapq.heappush(hp,ll1.val)
    heapq.heappush(hp,ll2.val)

    # while len(hp) > 0 :
    while hp:

        an = heapq.heappop(hp)

        print(an)
        if an == list1.val

    # n1 = Node(val = 9 )
    # n2 = Node(val = 11)
    # print(n1 < n2)