"""
1. 힙 (Heap) 이란?
- 힙: 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
- 완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

**힙을 사용하는 이유
- 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n) 이 걸림
- 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면, $ O(log n) $ 이 걸림
- 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

2. 힙 (Heap) 구조
- 힙은 최대값을 구하기 위한 구조 (최대 힙, Max Heap) 와, 최소값을 구하기 위한 구조 (최소 힙, Min Heap) 로 분류할 수 있음
- 힙은 다음과 같이 두 가지 조건을 가지고 있는 자료구조임
    1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
        최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음
    2. 완전 이진 트리 형태를 가짐

** 힙과 이진 탐색 트리의 공통점과 차이점
- 공통점: 힙과 이진 탐색 트리는 모두 이진 트리임
- 차이점:
    - 힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
    - 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
    - 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
        - 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
    - 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나로 이해하면 됨

    참고 :
    https://t3811573.p.clickup-attachments.com/t3811573/d9618f90-b438-4129-82f2-76f076328a47/Chapter11-%ED%9E%99-live.html?view=open
"""


class Heap:

    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):

        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        insert_idx = len(self.heap_array) - 1

        while self.move_up(insert_idx):
            parent_idx = insert_idx // 2
            self.heap_array[insert_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[
                insert_idx]
            insert_idx = parent_idx
        return True

    def move_down(self, pop_idx):
        left_child_idx = pop_idx * 2
        right_child_idx = pop_idx * 2 + 1

        if left_child_idx >= len(self.heap_array):
            return False
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[pop_idx] < self.heap_array[left_child_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                if self.heap_array[pop_idx] < self.heap_array[left_child_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[pop_idx] < self.heap_array[right_child_idx]:
                    return True
                else:
                    return False

    def pop(self):

        if len(self.heap_array) <= 1:
            return None

        return_data = self.heap_array[1]

        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            right_child_idx = popped_idx * 2 + 1
            left_child_idx = popped_idx * 2

            if right_child_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_idx] \
                        = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_idx
            else:
                if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                    if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_idx] \
                            = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_idx
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_idx] \
                            = self.heap_array[right_child_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_idx

        return return_data


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

heap.pop()
print(heap.heap_array)

heap.pop()
print(heap.heap_array)

heap.pop()
print(heap.heap_array)
