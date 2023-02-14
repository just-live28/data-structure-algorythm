def bubble_sort(array):

    for index in range(0,len(array)-1):
        for i in range(0, len(array)-index-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array
            
print(bubble_sort([1,91,37,52,63,7]))