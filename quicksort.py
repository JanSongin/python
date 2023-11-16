sort_list = [88,46,25,11,18,12,22]
#sort_list = [6,92,6,1,8,53,76]
def quicksort(unsorted):
    left_list = []
    middle_list = []
    right_list = []
    if (len(unsorted) <= 1):
        return unsorted
    else:
        pivot = unsorted[len(unsorted) - 1]
        count = 0
        while (len(unsorted) > count):
            if(pivot > unsorted[count]):
                left_list.append(unsorted[count])
            elif(pivot == unsorted[count]):
                middle_list.append(unsorted[count])
            elif(pivot < unsorted[count]):
                right_list.append(unsorted[count])
            count = count + 1
        return quicksort(left_list) + middle_list + quicksort(right_list)

sorted_list = quicksort(sort_list)
print(sorted_list)