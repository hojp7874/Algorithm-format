"""
재귀를 이용한 이진탐색
"""

def binary_search(array: list, target: int, left: int, right: int):
    print(left, right)
    if left >= right:
        raise("찾으려는 대상이 없습니다.")
    mid = (left + right) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, left, mid)
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, right)


# -----------------------------------------------------------------
if __name__ == "__main__":
    array = [1, 2, 5, 6, 8, 12]
    target = 4
    # --------------------Given

    left = 0
    right = len(array)
    print(binary_search(array, target, left, right))