# import sys
# sys.path.append(r"../Sequential Data Structures")

from sequentialDataStructures import linkedlist as ll 


def solve(head) :
        a = head
        try : 
            mid = head
            while head.next.next :
                head = head.next.next
                mid = mid.next
            
        except AttributeError : 
            mid = mid.next.next

        return a
    
if __name__ == "__main__" :
    l1 = ll.LinkedList()
    l1.insert_at(9,0)
    l1.insert_at_beginning(2)
    l1.insert_at_beginning(1)
    l1.insert_at_end(5)
    l1.insert_at(4,0)
    l1.insert_at_end(3)
    l1.insert_at(7,2)
    l1.display()
    print("done")
    
    d = solve(l1.head)
    
    while d :
        print(d.data, end = " " )
        d = d.next
        
    