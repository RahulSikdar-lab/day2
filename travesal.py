class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node(1)
node2 = Node(45)
node3 = Node(38)
node1.next = node2
node2.next = node3
current = node1
while current:
    print(current.data, end=" - ")
    current = current.next
print("None")
