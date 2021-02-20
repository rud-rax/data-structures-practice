

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
        
        if not self.check_valid_index(index): return 
                
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

    def check_valid_index(self,index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")
            return False
        return True
    
    def insert_at(self,index,data):
        
        if not self.check_valid_index(index) :
            return 
            
        
        if index == 0 :
            self.insert_at_beginning(data)
            return 

        itr = self.head
                
        for _ in range(0,index - 1):
            itr = itr.next
        insert_node = Node(data,itr.next)
        itr.next = insert_node

    def replace_at(self,index,data):

        if not self.check_valid_index(index) :
            return

        c = 0
        itr = self.head
        while itr :
            if c == index :
                itr.data = data
                break
            itr = itr.next
            c += 1 
    
    def find_value(self,value):
        itr = self.head
        c = 0
        value_exist = False
        while itr :
            if itr.data == value :
                value_exist = True
                break 
            itr = itr.next
            c+=1 

        if value_exist:
            print(f"VALUE FOUND AT {c}")
            return c
                
        else : 
            print("VALUE NOT FOUND !")
            return None

    def replace_value(self,old_value,new_value):
        
        value_index = self.find_value(old_value)

        if value_index:
            itr = self.head
            for _ in range(0 , value_index):
                itr = itr.next
            itr.data = new_value
            return True

        else :
            raise Exception("CANNOT REPLACE VALUE")

    def get_value_at(self,index):

        if not self.check_valid_index(index) : return 

        itr = self.head
        
        while index > 0 :
            index -= 1
            itr = itr.next

        return itr.data

            
        
        

if __name__ == "__main__": 

    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_end(4)
    ll.insert_at_end(1)
    ll.insert_at_beginning(2)
    ll.insert_at(2,3)

    ll.display()


    ll.replace_at(4,90)
    ll.find_value(5)
    ll.replace_value(5,222)
    m = 3
    print(f"VALUE AT {m} = {ll.get_value_at(m)}")

    ll.display()
