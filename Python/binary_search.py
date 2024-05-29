from typing import List

"""
BINARY SEARCH
- Time complexity: O(log n)
- Space complexity: O(1)

Instructions:
1. Set left and right pointers to the start and end of the array
2. While left pointer is less than or equal to right pointer
3. Calculate the middle index
4. If the middle element is the target, return the index
5. If the middle element is less than the target, move the left pointer to mid + 1
6. If the middle element is greater than the target, move the right pointer to mid - 1
7. If the target is not found, return -1
"""

def binary_search(arr: List[int], target:int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    print(binary_search(arr, target))
