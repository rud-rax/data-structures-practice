

class Node() :
    """
    Use to create a node of Doubly Linked List.

    1 data : Data to be assigned to the node
    2 prev : Address to the previous node in the Doubly Linked List (assigned to None by default)
    3 next : Address to the next node in the Doubly Linked List (assigned to None by default)
    """

    def __init__(self , data : int, prev = None, next = None) :
        self.data = data
        self.next = next
        self.prev = prev


def display(head : Node) :
    """
    Display all the elements present in the Doubly Linked List

    1 head : Head of the DLL
    """

    if not head :
        print("No elements in the Doubly Linked List")
    
    curnode = head

    while curnode :
        print(curnode.data , end = " -> ")
        curnode = curnode.next

    

def insert_at_beginning(head : Node, data : int) :
    """
    Creates and Node with data provided and inserts it at the beginning of the DLL.

    1 head : Head of the DLL
    2 data : Data to be inserted in the DLL
    """

    node = Node(data)

    if not head :
        return node

    head.prev = node
    node.next = head
    
    return node

def insert_at_end(head : Node , data : int) :
    """
    Creates a Node with data provided and inserts it at the end of the DLL.

    1 head : Head of the DLL
    2 data : Data to be inserted in the DLL
    """
    
    node = Node(data)

    if not head :
        return node

    curnode = head
    while curnode.next :
        curnode = curnode.next

    curnode.next = node
    node.prev = curnode

    return head


def delete_head(head : Node) :
    """
    Deletes the head of the DLL

    1 head : Head of the DLL
    """

    if not head :
        print("No elements in linked list present to delete.")
        return None

    head = head.next

    if head : 
        head.prev = None
 
    return head

def delete_last_node(head : Node) :
    """
    Deletes the last node of the DLL

    1 head : Head of the DLL
    """


    if not head :
        print("No elements in linked list present to delete.") 
        return None

    if not head.next :
        return None

    curnode = head

    while curnode.next :
        curnode = curnode.next

    curnode = curnode.prev
    curnode.next = None

    return head

def reverse(head : Node) :
    if not head :
        print("Doubly Linked List is empty.")
        return

    curnode = head

    while curnode :
        curnode.next,curnode.prev = curnode.prev , curnode.next
        previous_node = curnode
        curnode = curnode.prev

    return previous_node

if __name__ == "__main__" :
    # head = Node(10)
    # head.next = Node(20)
    # head.next.next = Node(30)
    # head.next.next.next = Node(40)

    # head.next.prev = head
    # head.next.next.prev = head.next
    # head.next.next.next.prev = head.next.next

    k = 4 # Number of nodes in DLL


    elelist = [40,30,20,10]
    head = None


    cur = head

    while k :

        if not cur : 
            cur = Node(elelist[k-1])

        else :
            cur.next = Node(elelist[k-1])
            cur.next.prev = cur
            cur = cur.next
                
        k-=1    