"""
버블 정렬 (bubble sort) 란?
두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘
"""

def bubbleSort(list):
    for idx in range(len(list) - 1):
        print(idx)
        swap = False
        for idx2 in range(len(list) - idx - 1):

            if list[idx2] > list[idx2 + 1]:
                list[idx2], list[idx2 + 1] = list[idx2 + 1], list[idx2]
                swap = True

        if swap is False:
            break

    return list

import random

data_list = random.sample(range(100), 50)
data_list1 = [5,4,3,2,1]

print (bubbleSort(data_list))
print(bubbleSort(data_list1))
