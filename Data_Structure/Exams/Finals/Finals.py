# 퀵정렬
# 중복 데이터, 마지막 킷값을 피벗, 내림차순으로 정렬하는 partition()함수 구현
# 전체 배열을 정렬하는 quick_sort()함수 구현
# 분할 단계별 결과와 최종 결과 출력
def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q - 1)
        quick_sort(A, q + 1, right)


def partition(A, left, right):
    low = left
    high = right - 1
    pivot = A[right]
    while (low <= high):
        while low <= right and A[low] > pivot:
            low += 1
        while high >= left and A[high] <= pivot:
            high -= 1

        if low < high:
            A[high], A[low] = A[low], A[high]

    A[right], A[low] = A[low], A[right]

    print("pivot = ", A[low], end="")
    print(" : ", A)

    return low


arr = [4, 1, 8, 3, 7, 3, 9, 6, 2, 5]
print("A Origin : ", arr)
quick_sort(arr, 0, len(arr) - 1)
print("A Sorted : ", arr)
