from random import shuffle

#list = [[i] for i in range(10)]
list = ["a","A","b","B","c","C"]
shuffle(list)
print("Unsorted array:")
print(list)

# Traverse through all array elements
for i in range(len(list)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(list)):
        if list[min_idx] > list[j]:
            min_idx = j

    # Swap the found minimum element with
    # the first element
    list[i], list[min_idx] = list[min_idx], list[i]

# Driver code to test above
print ("Sorted array:")
print(list)
