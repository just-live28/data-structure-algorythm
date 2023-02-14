def bubble_sort(array):
    last_index = len(array) - 1
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True
        for i in range(last_index):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                is_sorted = False
        last_index -= 1
    return array
            
print(bubble_sort([1,91,37,52,63,7]))