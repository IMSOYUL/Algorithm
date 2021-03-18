"""
1. 병합 정렬 (merge sort)
    재귀용법을 활용한 정렬 알고리즘
        - 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
        - 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
        - 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

2. 알고리즘 분석
    몇 단계 깊이까지 만들어지는지를 depth 라고 하고 i로 놓자. 맨 위 단계는 0으로 놓자.
        다음 그림에서 n/$2^2$ 는 2단계 깊이라고 해보자.
            - 각 단계에 있는 하나의 노드 안의 리스트 길이는 n/$2^2$ 가 된다.
            - 각 단계에는 $2^i$ 개의 노드가 있다.
    따라서, 각 단계는 항상 $2^i * \frac { n }{ 2^i } = O(n)$
    단계는 항상 $log_2 n$ 개 만큼 만들어짐, 시간 복잡도는 결국 O(log n), 2는 역시 상수이므로 삭제
    따라서, 단계별 시간 복잡도 O(n) * O(log n) = O(n log n)

참고
https://t3811573.p.clickup-attachments.com/t3811573/571f6996-bf8b-4452-9fb1-115212ae892a/Chapter15-%EA%B3%A0%EA%B8%89%EC%A0%95%EB%A0%AC-%EB%B3%91%ED%95%A9%EC%A0%95%EB%A0%AC-live.html?view=open
"""


def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    while len(left) > left_point and len(right) > right_point:

        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def mergesplit(data):
    if len(data) <= 1:
        return data

    mid = int(len(data) / 2)

    left = mergesplit(data[:mid])
    right = mergesplit(data[mid:])

    return merge(left, right)

import random

data_list = random.sample(range(100), 10)
print(data_list)
print(mergesplit(data_list))

