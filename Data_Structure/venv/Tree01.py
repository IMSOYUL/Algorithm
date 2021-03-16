
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        current_node = self.head
        while True:
            if value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
                    break
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    break

    def search(self,value):

        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            elif current_node.value > value :
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def delete(self, value):
        searched = False
        current_node = self.head
        parent = self.head

        while current_node:
            if current_node.value == value:
                searched = True
                break
            elif current_node.value > value:
                parent = current_node
                current_node = current_node.left
            else:
                parent = current_node
                current_node = current_node.right

        if searched is False:
            return False

        if current_node.left == current_node.right is None:
            if value < parent.value:
                parent.left = None
            else:
                parent.right = None

            del current_node

        elif current_node.left is not None and current_node.right is None:
            if parent.value > value:
                parent.left = current_node.left
            else:
                parent.right = current_node.left
        elif current_node.left is None and current_node.right is not None:
            if parent.value > value:
                parent.left = current_node.rignt
            else:
                parent.right = current_node.right

        elif current_node.left is not None and current_node.right is not None:
            if value < parent.value:
                change_node = current_node.right
                change_node_parent = current_node.right

                while change_node.left is not None:
                    change_node_parent = change_node
                    change_node = current_node.left

                if change_node.right is not None:
                    change_node_parent.left = change_node.right
                else:
                    change_node_parent.left = None

                parent.left = change_node
                change_node.right = current_node.right
                change_node.left = current_node.left
            else:
                change_node = current_node.right
                change_node_parent = current_node.right

                while change_node.left is not None:
                    change_node_parent = change_node
                    change_node = current_node.left

                if change_node.right is not None:
                    change_node_parent.left = change_node.right
                else:
                    change_node_parent.left = None

                parent.right = change_node
                change_node.left = current_node.left
                change_node.right = current_node.right






head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(4))