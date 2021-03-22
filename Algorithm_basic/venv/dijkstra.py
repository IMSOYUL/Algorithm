
"""
* 최단 경로 문제란?
    최단 경로 문제란 두 노드를 잇는 가장 짧은 경로를 찾는 문제임
    가중치 그래프 (Weighted Graph) 에서 간선 (Edge)의 가중치 합이 최소가 되도록 하는 경로를 찾는 것이 목적
* 최단 경로 문제 종류
    - 단일 출발 및 단일 도착 (single-source and single-destination shortest path problem) 최단 경로 문제
        : 그래프 내의 특정 노드 u 에서 출발, 또다른 특정 노드 v 에 도착하는 가장 짧은 경로를 찾는 문제
    - 단일 출발 (single-source shortest path problem) 최단 경로 문제  ===> 다익스트라 알고리
        : 그래프 내의 특정 노드 u 와 그래프 내 다른 모든 노드 각각의 가장 짧은 경로를 찾는 문제
            따지고 보면 굉장히 헷깔릴 수 있으므로 명확히 하자면, 예를 들어 A, B, C, D 라는 노드를 가진 그래프에서 특정 노드를 A 라고 한다면,
            A 외 모든 노드인 B, C, D 각 노드와 A 간에 (즉, A - B, A - C, A - D) 각각 가장 짧은 경로를 찾는 문제를 의미함
* 다익스트라 알고리즘 로직
    첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신하는 기법
    다익스트라 알고리즘은 너비우선탐색(BFS)와 유사
        첫 정점부터 각 노드간의 거리를 저장하는 배열을 만든 후, 첫 정점의 인접 노드 간의 거리부터 먼저 계산하면서, 첫 정점부터 해당 노드간의 가장 짧은 거리를 해당 배열에 업데이트
        다익스트라 알고리즘의 다양한 변형 로직이 있지만, 가장 개선된 우선순위 큐를 사용

    ** 우선순위 큐를 활용한 다익스트라 알고리즘
        우선순위 큐는 MinHeap 방식을 활용해서, 현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 됨
            1) 첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장
                - 초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장함 (inf 라고 표현함)
                - 우선순위 큐에 (첫 정점, 거리 0) 만 먼저 넣음
            2) 우선순위 큐에서 노드를 꺼냄
                - 처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐
                - 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교한다.
                - 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트한다.
                - 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다.
                    결과적으로 너비 우선 탐색 방식과 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨
                    만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 거리(루트)를 가진 (노드, 거리)의 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음
            3) 2번의 과정을 우선순위 큐에 꺼낼 노드가 없을 때까지 반복한다.

참고 : https://t3811573.p.clickup-attachments.com/t3811573/75182ca7-01ea-48f7-a85e-811a5ecda972/Chapter20-%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9D%B4%ED%95%B4-live.html?view=open

"""


import heapq


mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):

    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue,[distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distances[adjacent] > distance:
                distances[adjacent] = distance
                heapq.heappush(queue,[distance, adjacent])

    return distances

print(dijkstra(mygraph, 'A'))


def dijkstra2(graph, start, end):

    distances = {vertex: [float('inf'), start] for vertex in graph}

    distances[start] = [0,start]

    queue = []

    heapq.heappush(queue,[distances[start][0], start])

    while queue:

        current_distance, current_vertex = heapq.heappop(queue)

        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():

            distance = current_distance + weight

            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_out = end + '->'
    while distances[path][1] != start:
        path_out  += distances[path][1] + '->'
        path = distances[path][1]
    path_out += start
    print(path_out)
    return distances

print(dijkstra2(mygraph, 'A', 'F'))

"""
* 시간 복잡도
    - 위 다익스트라 알고리즘은 크게 다음 두 가지 과정을 거침
        # 과정1: 각 노드마다 인접한 간선들을 모두 검사하는 과정
        # 과정2: 우선순위 큐에 노드/거리 정보를 넣고 삭제(pop)하는 과정
        
    - 각 과정별 시간 복잡도
        # 과정1: 각 노드는 최대 한 번씩 방문하므로 (첫 노드와 해당 노드간의 갈 수 있는 루트가 있는 경우만 해당), 그래프의 모든 간선은 최대 한 번씩 검사
            즉, 각 노드마다 인접한 간선들을 모두 검사하는 과정은 O(E) 시간이 걸림, E 는 간선(edge)의 약자
        # 과정2: 우선순위 큐에 가장 많은 노드, 거리 정보가 들어가는 경우, 우선순위 큐에 노드/거리 정보를 넣고, 삭제하는 과정이 최악의 시간이 걸림
            우선순위 큐에 가장 많은 노드, 거리 정보가 들어가는 시나리오는 그래프의 모든 간선이 검사될 때마다, 배열의 최단 거리가 갱신되고, 우선순위 큐에 노드/거리가 추가되는 것임
            이 때 추가는 각 간선마다 최대 한 번 일어날 수 있으므로, 최대 O(E)의 시간이 걸리고, O(E) 개의 노드/거리 정보에 대해 우선순위 큐를 유지하는 작업은 $ O(log{E}) $ 가 걸림
            따라서 해당 과정의 시간 복잡도는 $ O(Elog{E}) $
* 총 시간 복잡도
    # 과정1 + 과정2 = O(E) + $ O(Elog{E}) $ = $ O(E + Elog{E}) = O(Elog{E}) $
* 참고: 힙의 시간 복잡도
    depth (트리의 높이) 를 h라고 표기한다면,
    n개의 노드를 가지는 heap 에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로 h=log2n 에 가까우므로, 시간 복잡도는 O(logn)
"""