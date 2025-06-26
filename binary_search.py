def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) 

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  

arr = [1, 3, 5, 7, 9, 11]
target = 3

result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at position {result}")
else:
    print(f"Element {target} not found in the array")