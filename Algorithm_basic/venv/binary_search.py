"""
2. 분할 정복 알고리즘과 이진 탐색
    분할 정복 알고리즘 (Divide and Conquer)
        Divide: 문제를 하나 또는 둘 이상으로 나눈다.
        Conquer: 나눠진 문제가 충분히 작고, 해결이 가능하다면 해결하고, 그렇지 않다면 다시 나눈다.
이진 탐색
    Divide: 리스트를 두 개의 서브 리스트로 나눈다.
    Comquer
        검색할 숫자 (search) > 중간값 이면, 뒷 부분의 서브 리스트에서 검색할 숫자를 찾는다.
        검색할 숫자 (search) < 중간값 이면, 앞 부분의 서브 리스트에서 검색할 숫자를 찾는다.
5. 알고리즘 분석
    n개의 리스트를 매번 2로 나누어 1이 될 때까지 비교연산을 k회 진행
        n X $\frac { 1 }{ 2 }$ X $\frac { 1 }{ 2 }$ X $\frac { 1 }{ 2 }$ ... = 1
        n X $\frac { 1 }{ 2 }^k$ = 1
        n = $2^k$ = $log_2 n$ = $log_2 2^k$
        $log_2 n$ = k
        빅 오 표기법으로는 k + 1 이 결국 최종 시간 복잡도임 (1이 되었을 때도, 비교연산을 한번 수행)
            결국 O($log_2 n$ + 1) 이고, 2와 1, 상수는 삭제 되므로, O($log n$)
참고
https://t3811573.p.clickup-attachments.com/t3811573/0ac052d3-8a65-43e0-b4ed-5921aa204eef/Chapter16-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89-live.html?view=open
"""

def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    mid = len(data) //2

    if search == data[mid]:
        return True
    else:
        if search > data[mid]:
            return binary_search(data[mid+1:], search)
        else:
            return binary_search(data[:mid], search)


import random
data_list = [1,2,3,4,5,6,7,8,9]

print(binary_search(data_list, 10))