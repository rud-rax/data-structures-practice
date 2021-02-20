

class Node :
    def __init__(self,data = None , next = None):
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self):
        self.head = None
    
    def length(self): 
        c = 0
        itr = self.head

        while itr:
            c+=1
            itr = itr.next
        
        return c

    def display(self,index = 0):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")
            
        
        itr = self.head
        if index != 0:
            c = 0 
            while c != index - 1 :
                itr = itr.next
                c += 1
        
        ll_str = ""
        while itr :
            ll_str += str(itr.data) + " --> "
            itr = itr.next
        
        print(ll_str)
        

    def insert_at_beginning(self,data):

        self.head =  Node(data,self.head)

    def insert_at_end(self,data):
        
        if self.head :
            insert_node = Node(data)
            itr = self.head

            while itr.next:
                itr = itr.next
            
            else : itr.next = insert_node

        else : self.head = Node(data)

    def insert_at(self,index,data):
        if index < 0 or index > self.length():
            raise Exception("Invalid index")
            
        
        if index == 0 :
            self.insert_at_beginning(data)
            return 

        itr = self.head
                
        for _ in range(0,index - 1):
            itr = itr.next
        insert_node = Node(data,itr.next)
        itr.next = insert_node

if __name__ == "__main__": 

    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_end(4)
    ll.insert_at_end(1)
    ll.insert_at_beginning(2)
    ll.insert_at(4,3)
    ll.display()
