import quicksortExe as QuickSort

def linearSearch(target, arr):
    
    for i in range(0, len(arr)):
        
        target_position = i + 1 if target > arr[i] else target_position
    
        if arr[i] == target:
            return i

    return target_position

def binary_search(target, arr):
    i = 0
    j = len(arr) - 1

    while i <= j:
        m = (i + j) // 2
        temp = arr[m]
        
        if temp == target:
            return m
        
        if temp < target:
            i = m + 1
        else:
            j = m - 1 
    return i
        
    
arr = [12,34,55,45,67,87,1,3,5,7,86,24,33,4,2]

QuickSort.quicksort(arr)
print(arr)

print(linearSearch(53, arr))

print(binary_search(53, arr))

