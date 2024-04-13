from collections import Counter
import heapq
 
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
         
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def makeHeap(text) : 
    nodes = []
    
    co = Counter(text).most_common()
    print(co)
    for char , freq in co:
        heapq.heappush(nodes, node(freq,char))
    
    while len(nodes) > 1:
        

        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    
        heapq.heappush(nodes, newNode)
        
    return nodes[0]


def printNodes(node, val=''):

    newVal = val + str(node.huff)

    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
 

    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")


if __name__ == "__main__" :

    root = makeHeap('BAACCCD')
    printNodes(root)