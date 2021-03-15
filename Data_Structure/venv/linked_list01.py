"""
1. 링크드 리스트 (Linked List) 구조¶
연결 리스트라고도 함
배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
본래 C언어에서는 주요한 데이터 구조이지만, 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원

링크드 리스트 기본 구조와 용어

노드(Node): 데이터 저장 단위 (데이터값, 포인터) 로 구성
포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:

    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):

        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head

        while node:
            print(node.data)
            node = node.next

    def delete(self, data):

        if self.head is None:
            print("노드가 없습니다.")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    def search_node(self, data):

        node = self.head

        while node:
            if node.data == data:
                return node
            else:
                node = node.next




# 테스트
node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.add(data)

node = node_mgmt.search_node(4)
print (node.data)
