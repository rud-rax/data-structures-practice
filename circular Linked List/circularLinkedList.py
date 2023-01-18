class Node() :
    """
    Generate a node of a linked list

    1 data : Data of linked list
    2 next : Next node of the linked list, assigned None by default
    """
    def __init__(self,data,next = None) -> None:
        self.data = data
        self.next = next


def display(head : Node) :
    '''
    Displays all the elements present in the linked list
    '''
    

    if not head :
        return 

    curnode = head
    print(curnode.data)
    curnode = curnode.next

    while curnode != head :
        print(curnode.data)
        curnode = curnode.next

def insert_at_beginning(head : Node, node : Node ) :
    """
    Inserts a Node at the beginning

    1 node : Node to be inserted in the circular linked list , node will be inserted in the beginning
    """

    if not head :
        head = node
        head.next = head
        return head

    curnode = head

    while curnode.next != head :
        curnode = curnode.next

    curnode.next,node.next = node,curnode.next
    head = node
    return head

def insert_at_beginning2(head : Node,node : Node) :
    """
    Inserts a Node at the beginning of the circular linked list

    1 node : Node to be inserted in the circular linked list at beginning
    """

    if not head :
        head = node
        head.next = head
        return head

    head.next,node.next = node,head.next 
    head.data,node.data = node.data,head.data

    return head

def insert_at_end(head : Node, node : Node) :
    """
    Inserts a Node at the end of the circular linked list
    
    1 node : node to be inserted in the circular linked list at end
    """

    if not head :
        head = node
        head.next = head
        return head

    head.data, node.data = node.data ,head.data
    head.next,node.next = node,head.next
    head = node

    return head

def delete_at_head(head : Node) :
    
    if not head :
        return None

    if head.next == head :
        return None

    head.data = head.next.data
    head.next = head.next.next

    return head

        

if __name__ == "__main__" :
    


    # creating a cll
    # 10 - 5 - 15 - 30

    # cll = CircularLinkedList()
    
    head = Node(10)
    head.next = head
    # head.next = Node(5)
    # head.next.next = Node(15)
    # head.next.next.next = Node(30)
    # head.next.next.next.next = head

    # display the data in cll
    display(head)





    