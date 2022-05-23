#Given an array of numbers, sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def sort_array(source_array):
    newList = sorted([n for n in source_array if n%2 != 0])
    odd = 0
    
    for i in range(len(source_array)):
        if source_array[i] %2 != 0:
            source_array[i] = newList[odd]
            odd += 1
            
    return source_array

sort_array([5, 3, 2, 8, 1, 4])    
