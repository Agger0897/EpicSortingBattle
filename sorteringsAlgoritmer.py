from random import shuffle

alist = ["3","6","2","5","7","3","3","6"]

def selectionSort(list):


    # Traverse through all array elements
    for i in range(len(list)):

    # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j

    # Swap the found minimum element with the first element
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

print(selectionSort(alist))
