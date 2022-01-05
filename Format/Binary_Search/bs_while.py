"""
반복문을 이용한 이진탐색
"""

def binary_search(array: list, target: int):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid
        elif target > array[mid]:
            left = mid + 1
    raise("찾으려는 대상이 없습니다.")

# ------------------------------------------
if __name__ == "__main__":
    array = [1, 2, 4, 5, 7, 12]
    target = 5
    # --------------------Given

    print(binary_search(array, target))