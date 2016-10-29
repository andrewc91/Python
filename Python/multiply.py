a = [2, 4, 10, 16]

def multiply(arr):
    for i in range(len(a)):
        a[i] = a[i] * 5
    return arr

b = multiply(a)
print b
