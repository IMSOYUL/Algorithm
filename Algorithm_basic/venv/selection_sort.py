"""
1. 선택 정렬 (selection sort) 란?
다음과 같은 순서를 반복하며 정렬하는 알고리즘
주어진 데이터 중, 최소값을 찾음
해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

알고리즘 분석
반복문이 두 개 O($n^2$)
실제로 상세하게 계산하면, $\frac { n * (n - 1)}{ 2 }$
"""


def selection_sort(data):

    for stand in range(len(data) - 1):
        lowest = stand
        for idx in range(stand + 1, len(data)):
            if data[lowest] > data[idx]:
                lowest = idx
        data[lowest], data[stand] = data[stand], data[lowest]
    return data


list = [7,6,5,4,3,2,1]
print(selection_sort(list))