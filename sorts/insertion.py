def insertion(lst):
    for i in range(1, len(lst)):
        unsorted_item = i
        sorted_item = unsorted_item - 1
        while sorted_item > -1 and lst[sorted_item] > lst[sorted_item+1]:
            lst[sorted_item], lst[sorted_item + 1] = lst[sorted_item + 1], lst[sorted_item]
            sorted_item -= 1
