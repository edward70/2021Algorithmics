lst = [1,6,7,8,21,45]

def binarySearch(target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binarySearch(target, low, mid-1)
    elif lst[mid] < target:
        return binarySearch(target, mid+1, high)

print(binarySearch(7, 0, len(lst) - 1))
