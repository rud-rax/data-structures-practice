
class Node :
    def __init__(self,data = None,next = None , forward = None):
        self.next = next
        self.forward = forward
        self.data = data

class SkipList :

    def __init__(self,length):
        
        self.head = None
        #self.head = None
        #self.next = None
        #self.ff = None

    def length(self):

        l = 0
        itr = self.head

        while itr :
            l+=1
            itr = itr.next

        return l

    def insert(self,data,index = None):
    
        if index == 0 or self.length() == 0:
            
            self.head = Node(data,self.head)
           
        else : 

     
            if not index : index = self.length()  # if no index is specified data will be inserted at the end
            
            elif index > self.length(): 
                print("INVALID INDEX")
                return 

            itr = self.head

            while index > 1  :
                itr = itr.next
                index -= 1
            else :
                insert_node = Node(data , itr.next , itr.forward)
                itr.next = insert_node


    def display(self):

        str_list = "" 
        itr = self.head

        while itr :

            str_list += str(itr.data) + " -> "
            itr = itr.next
        
        print(str_list)

        return str_list

if __name__ == "__main__":

    skiplist1 = SkipList(10)
    skiplist1.insert(10)
    skiplist1.insert(20)

    skiplist1.insert(40)
    skiplist1.display()
    skiplist1.insert(30,2)
    skiplist1.display()
    print(skiplist1.length())


