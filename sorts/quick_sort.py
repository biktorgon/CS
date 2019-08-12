def partition(lst, left, right):
    pivot = lst[(left + right) // 2]
    left -= 1
    right += 1
    while True:
        left += 1
        right -= 1
        while lst[left] < pivot:
            left += 1
        while lst[right] > pivot:
            right -= 1
        
        if left >= right:
            return right

        lst[left], lst[right] = lst[right], lst[left]


def quick_sort(lst, start, end):
    if start < end:
        split_index = partition(lst, start, end)
        quick_sort(lst, start, split_index)
        quick_sort(lst, split_index +1, end)
