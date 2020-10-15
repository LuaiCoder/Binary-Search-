
def binarysearch (array,target):
    arr = bub(array)
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

        else:
            return mid

    return -1

def bub(array):
    n = len(array)
    sot = False

    while not sot:
            sot = True
            for i in range (n-1):
                if array[i] > array[i+1]:
                    swap(i,i+1,array)
                    sot = False
    return (array)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

arr =  [23, 25, 65, 24, 58, 69, 95, 31, 5, 7, 44, 27, 32]
target = 95

res = binarysearch(arr,target)

if res != -1:
        print("Element is present at index", str(res))
else:
        print("Results not found")



