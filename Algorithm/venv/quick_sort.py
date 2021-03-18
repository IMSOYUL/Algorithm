"""
대표적인 정렬5: 퀵 정렬 (quick sort)¶

- 퀵 정렬 (quick sort) 이란?¶
    - 정렬 알고리즘의 꽃
    - 기준점(pivot 이라고 부름)을 정해서, 기준점보다 작은 데이터는 왼쪽(left), 큰 데이터는 오른쪽(right) 으로 모으는 함수를 작성함
    - 각 왼쪽(left), 오른쪽(right)은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
    - 함수는 왼쪽(left) + 기준점(pivot) + 오른쪽(right) 을 리턴함


- 알고리즘 분석
    - 병합정렬과 유사, 시간복잡도는 O(n log n)
    - 단, 최악의 경우
        맨 처음 pivot이 가장 크거나, 가장 작으면
        모든 데이터를 비교하는 상황이 나옴
        O($n^2$)
"""


def qsort(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for idx in range(1, len(data)):
        if pivot > data[idx]:
            left.append(data[idx])

        else:
            right.append(data[idx])

    return qsort(left) + [pivot] + qsort(right)


import random

data_list = random.sample(range(100), 10)

print(data_list)
print(qsort(data_list))

"""
list comprehension을 사용해서 더 깔끔하게 작성
"""


def qsort2(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort2(left) + [pivot] + qsort2(right)

data_list = random.sample(range(100), 10)

print(data_list)
print(qsort2(data_list))