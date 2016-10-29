def bubbleSort(arr):
    length = len(arr) - 1
    while length >= 1:
        for element in range(0, length):
            if arr[element] > arr[element + 1]:
                arr[element + 1], arr[element] = arr[element], arr[element + 1]
        length -= 1
    print arr

bubbleSort([1,3,5,2,6,7,3])
