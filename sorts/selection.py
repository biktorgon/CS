def selection(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]
