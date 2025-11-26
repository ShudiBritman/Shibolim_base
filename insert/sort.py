def bobble_sort(arr):
    for i in range(len(arr)):
        unsorted = True
        for j in range(0, len(arr) - i - 1):
            if arr[j].distance < arr[j+1].distance:
                swap(arr, j, j+1)
                unsorted = False
        if unsorted:
            break
    return arr



def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


