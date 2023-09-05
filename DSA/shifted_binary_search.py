import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

def shifted_binary(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        middle = low + (high - low) // 2

        if target == array[middle]:
            return middle
        
        elif array[low] <= array[middle]:
            if target < array[middle] and target >= array[low]:
                high = middle - 1 # eliminates right half
            else:
                low = middle + 1 # eliminates left half
        else:
            if target > array[middle] and target < array[high]:
                low = middle + 1 # eliminates left half
            else:
                high = middle + 1 # eliminates right hal
    return -1

if __name__ == "__main__":
    array = [9, 19, 1, 2, 7]
    target = 19

    find_target = shifted_binary(array, target)
    
    if find_target == -1:
        logging.debug('Target not found in array!')
    else:
        logging.debug(f'Target Found at index {find_target}')