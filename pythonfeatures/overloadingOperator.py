

class Node() :
    def __init__(self , freq : int = 0 ) :
        self.freq = freq
        
    def __lt__(self , node) :
        return self.freq < node.freq
    
if __name__ == "__main__" :
    
    a = Node(3)
    b = Node(6)
    
    print(a < b)