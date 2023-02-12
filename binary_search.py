def binary_search(array, search_value):
    
# list = [1,2,3,4,5]

    first_cell = 0
    last_cell = len(array) - 1
    
    mid_cell = int((first_cell + last_cell) / 2)
    
    while last_cell - first_cell > 0:
        if search_value == array[mid_cell]:
            return mid_cell
        elif search_value > array[mid_cell]:
            first_cell = mid_cell + 1
            mid_cell = int((first_cell + last_cell) / 2)
        else:
            last_cell = mid_cell - 1
            mid_cell = int((first_cell + last_cell) / 2)
    
    if search_value == array[mid_cell]:
        return mid_cell
    else:
        return None

r1 = binary_search([1,3,6,10,17,24,31,40,59],40)
print(r1)
