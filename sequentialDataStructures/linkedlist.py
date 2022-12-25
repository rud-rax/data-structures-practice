
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail
        self.length = 0

    def insert_at_beginning(self,data):
        node = Node(data)
        self.length +=1
        if self.head :
            node.next = self.head
            
        self.head = node

        if not self.tail  :
            self.tail = self.head

        

    def insert_at_end(self,data):
        self.length +=1
        node= Node(data)

        if self.tail:
            self.tail.next = node
            self.tail = node 

        else : self.tail = node

    def insert_at(self,data,index):

        if not self.valid_index(index):
            raise IndexError
            return 
        
        if index == 0 :
            self.insert_at_beginning(data)
            return

        
        if index == self.length :
            self.insert_at_end(data)
            
            return

        itr = self.head
        for _ in range(index -1 ):
            itr = itr.next
             
        
        itr.next = Node(data,itr.next)
        self.length+=1

    def display(self):
        itr = self.head
        while itr :
            print(f"{itr.data} --> ",end='')
            itr = itr.next
        print()

    def delete_node(self,index):

        if not self.valid_index(index) : 
            raise IndexError
            return 

        if index == 0 :
            self.head = self.head.next
            return

        itr = self.head
        for _ in range(index - 1):
            itr = itr.next

        itr.next = itr.next.next
        if index == self.length - 1:
            self.tail = itr 
        self.length -=1 
    
    def replace_value_at(self,data,index):
        if not self.valid_index(index) :
            raise IndexError
            return

        itr = self.head
        for _ in range(index):
            itr = itr.next
        itr.data = data

    def valid_index(self,index):
        if index < 0: return False
        elif index == 0  and not self.head: return True 
        elif index > self.length :return False

        return True
        
    def get_value_at(self,index):
        if not self.valid_index(index) :
            raise IndexError
            return

        itr = self.head
        for _ in range(index):
            itr = itr.next

        return itr.data 
        
    def find_value(self,value):
        index = 0
        itr = self.head 
        while itr :
            if itr.data == value: 
                print(f"VALUE FOUND AT {index}")
                return index
            index +=1
            itr = itr.next

        print("VALUE NOT FOUND !")
        return False

    def reverse(self) :

        prenode = None
        curnode = self.head

        while curnode :

            nexnode = curnode.next
            curnode.next = prenode
            prenode = curnode
            curnode = nexnode

        self.head = prenode

        

if __name__ == "__main__":
    l1 = LinkedList()

    l1.insert_at(9,0)
    l1.insert_at_beginning(2)
    l1.insert_at_beginning(1)
    l1.insert_at_end(5)
    l1.insert_at(4,0)
    l1.insert_at_end(3)
    l1.insert_at(7,2)
    l1.display()
    print("\nLENGTH OF LINKED LIST : ",l1.length)
    l1.delete_node(l1.length -1)
    l1.display()
    l1.replace_value_at(8,2)
    l1.display()
    print("\nLENGTH OF LINKED LIST : ",l1.length)

    i = 4
    print(f"VALUE AT {i} IS : {l1.get_value_at(i)}")
    l1.insert_at_end(14)
    l1.insert_at(11,6)
    l1.display()
    print("\nLENGTH OF LINKED LIST : ",l1.length)

    l1.reverse()
    l1.display()
   