def quicksort(array):
    lower = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                lower.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(lower) + equal + quicksort(greater)
    else:
        return array

print(quicksort([5, 2, 3, 1, 4]))
