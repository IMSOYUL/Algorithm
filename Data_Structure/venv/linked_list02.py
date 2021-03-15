"""
더블 링크드 리스트(Doubly linked list) 기본 구조
이중 연결 리스트라고도 함
장점: 양방향으로 연결되어 있어서 노드 탐색이 양쪽으로 모두 가능
"""


class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:

    def __init__(self, data):

        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):

        if self.head is None:
            self.head = Node(data)
            self.tail = helf.head
        else:
            node = self.head
            while node.next:
                node = node.next

            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head

        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):

        if self.head is None:
            return False

        node = self.head

        while node:
            if node.data == data:
                return node
            else:
                node = node.next

        return False

    def search_from_tail(self, data):
        if self.head is None:
            return False

        node = self.tail

        while node:
            if node.data == data:
                return node
            else:
                node = node.prev

        return False

    def insert_before(self, data, before_data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node is None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True

    def insert_after(self, data, after_data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node is None:
                    return False
            new = Node(data)
            after_new = node.next
            new.prev = node
            new.next = after_new
            node.next = new
            if new.next is None:
                slef.tail = new
            return True

            return True



double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()

print("===============================")

double_linked_list.insert_before(1.5, 2)
double_linked_list.desc()

print("===============================")


double_linked_list.insert_after(1.8, 1)
double_linked_list.desc()