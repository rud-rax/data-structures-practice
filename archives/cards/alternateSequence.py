class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = next


def makeCLL(n):
    head = Node()
    node = head

    for _ in range(n - 1):
        node.next = Node()
        node = node.next

    node.next = head

    return head


def makeSequence(head, n=13):
    royalCards = {1: "A", 11: "J", 12: "Q", 13: "K"}

    node = head
    i = 1
    while True:
        if i in royalCards.keys():
            node.data = royalCards[i]
        else:
            node.data = i

        if i == 13:
            break

        for _ in range(2):
            node = node.next

            while node.data:
                node = node.next

        i += 1

    n -= 1
    while n:
        head = head.next
        n -= 1

    return head


def displayList(head):
    stopAt = head.data
    node = head

    print(f"{node.data} -> ", end="")
    node = node.next

    while not node.data == stopAt:
        print(f"{node.data} -> ", end="")
        node = node.next


n = 13
head = makeCLL(n)
head = makeSequence(head, n)
displayList(head)
