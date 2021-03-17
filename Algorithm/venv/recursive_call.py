"""
재귀 용법 (recursive call, 재귀 호출)
고급 정렬 알고리즘엥서 재귀 용법을 사용하므로, 고급 정렬 알고리즘을 익히기 전에 재귀 용법을 먼저 익히기로 합니다.

1. 재귀 용법 (recursive call, 재귀 호출)
함수 안에서 동일한 함수를 호출하는 형태
여러 알고리즘 작성시 사용되므로, 익숙해져야 함

참고
- https://t3811573.p.clickup-attachments.com/t3811573/5fb93c23-ff65-4b3a-8482-cfb3e54ff5b7/Chapter13-%EC%9E%AC%EA%B7%80%EC%9A%A9%EB%B2%95-live.html?view=open

"""


def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num


for num in range(10):
    print(factorial(num))


def multiple(num):
    if num <= 1:
        return num
    else:
        return num * multiple(num - 1)

print(multiple(10))

def sum_list(data):

    if len(data) <=1:
        return data[0]
    else:
        return data[0] + sum_list(data[1:])

import random
data = random.sample(range(100), 10)
print(data)
print(sum_list(data))