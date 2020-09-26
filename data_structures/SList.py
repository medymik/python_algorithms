class Node:
    def __init__(self, value: str) -> None:
        self.next = None
        self.value = value
    def __str__(self) -> str:
        return self.value

class SList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_back(self, node: Node) -> None:
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_front(self, node: Node) -> None:
        if self.head == None:
            self.add_back(node)
        else:
            node.next = self.head
            self.head = node

    def reverse(self) -> None:
        if self.head != None:
            prev = self.head
            if prev.next != None:
                current = prev.next
                prev.next = None
                while current != None:
                    tmp = current
                    current = current.next
                    tmp.next = prev
                    prev = tmp
                    self.head = tmp

    def __str__(self) -> str:
        _str = 'Head -> '
        tmp = self.head
        while tmp != None:
            _str += str(tmp) + ' -> '
            tmp = tmp.next
        _str += 'None'
        return _str
