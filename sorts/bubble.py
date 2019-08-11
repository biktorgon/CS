def bubble(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(lst)):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                swapped = True
