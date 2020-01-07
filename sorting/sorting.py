A = [1, 3, 4, 2]

def bubbleSort(list):
    for i in list:
        if list[i] == len(list) - 1:
            continue
        elif i > list[list[i]+1]:
             list[list[i]], list[list[i]+1] = list[list[i]+1], list[list[i]]
    return list

bubbleSort(A)