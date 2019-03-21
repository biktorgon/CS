from sorts.swap import swap


def bubble(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(lst)):
            if lst[i-1] > lst[i]:
                swap(lst, i-1, i)
                swapped = True
