
import sys

import linkedlist as ll


def  solve(head, n) : 

        node = head
        ll = [node] 
        i = 0 
        while node :
            i+=1
            ll.append(node.next)

            if not i <= n + 1: 
                ll.pop(0)
            node = node.next

        node = ll[0]
        if n > 1 :
            node = node.next.next 
        else :
            node = None
        

        return head
                
if __name__ == "__main__" :

    li = ll.LinkedList()
    li.insert_at_beginning(1)
    li.insert_at_end(2)
    li.insert_at_end(3)
    li.insert_at_end(4)
    li.insert_at_end(5)

    li.display()

    node = solve(li.head , n = 2 )

    while node : 
        print(node.data)
        node = node.next

    