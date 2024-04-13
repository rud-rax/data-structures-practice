
import linkedlist as ll

class Stack:
    def __init__(self):
        self.head = ll.LinkedList()
        self.length = self.head.length

    def push(self,data):
        self.head.insert_at_beginning(data)

    def pop(self):
        value = self.head.get_value_at(0)
        self.head.delete_node(0)
        return value

    def display(self):
        self.head.display()

if __name__ == "__main__":
    s1 = Stack()
    s1.push(5)
    s1.display()
    s1.push(2)
    s1.push(4)
    s1.pop()
    s1.push(9)
    s1.display()    

    
    