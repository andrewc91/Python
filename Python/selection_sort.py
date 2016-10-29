def selection_sort(arr):
    current = 0
    min = 0

    while current < len(arr):
        for num in range(current, len(arr)):
            if arr[num] < arr[min]:
                min = num
        arr[current], arr[min] = arr[min], arr[current]
        current += 1
        min = current
    print arr


selection_sort([1,2,6,7,3,5])
