from sorts.swap import swap


def buble(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(lst)-1):
            if lst[i-1] > lst[i]:
                swap(lst, i-1, i)
                swapped = True
