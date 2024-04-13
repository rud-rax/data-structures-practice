

class TreeNode :
    def __init__(self,data,left = None,right = None) :
        self.data = data
        self.left = left
        self.right = right

class BST :
    def __init__(self,root) :
        self.root = root
    
    

def recursiveSearch(value , root) :

    if not root :
        return False
    
    if root.data == value :
        return True
    elif root.data > value :
        return recursiveSearch(value , root.left)
    else :
        return recursiveSearch(value,root.right)


def iterativeSearch(value , root) :

    node = root
    while node :
        if value == node.data :
            return True
        elif value < node.data :
            node = node.left
        else :
            node = node.right
    return False


def insertInBST(root : TreeNode , value : int) -> TreeNode :

    if not root :
        return TreeNode(value)

    node = root
    while node :
        if value == node.data :
            break
        elif value < node.data :
            if not node.left :
                node.left = TreeNode(value)
                break
            else :
                node = node.left
        else :
            if not node.right :
                node.right = TreeNode(value)
                break
            else :
                node = node.right 
    

    return root

def deleteInBST(root , value ) :
    pass



def display(root : TreeNode) -> None:
    node = root
    queue = [node]

    while queue :
        node = queue.pop(0)
        if node.left :
            queue.append(node.left)
        if node.right :
            queue.append(node.right)

        print(node.data)


if __name__ == "__main__" :
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.left.left = TreeNode(5)
    root.right = TreeNode(40)
    root.right.left = TreeNode(30)
    root.right.right = TreeNode(80)
    root.right.right.left = TreeNode(50)
    root.right.right.right = TreeNode(100)

    # print(recursiveSearch(11,root))
    # print(iterativeSearch(11,root))

    print("BEFORE INSERTION : ")
    display(root)
    root = insertInBST(root,1)
    print("AFTER INSERTION : ")
    display(root)

