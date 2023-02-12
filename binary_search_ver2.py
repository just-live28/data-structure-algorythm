def binary_search(array, search_value):
    
    first_cell = 0
    last_cell = len(array) - 1
    
    while last_cell - first_cell >= 0:
        mid_cell = int((first_cell + last_cell) / 2)
        mid_cell_value = array[mid_cell]
        
        if search_value == mid_cell_value:
            return mid_cell
        elif search_value > mid_cell_value:
            first_cell = mid_cell + 1
        else:
            last_cell = mid_cell - 1
    
    return None

r1 = binary_search([1,3,6,10,17,24,31,40,59],59)
print(r1)
