import numpy as np

sudoku = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 4, 5, 6, 7, 8, 9, 1, 2], [4, 5, 6, 7, 8, 9, 1, 2, 3], [5, 6, 7, 8, 9, 1, 2, 3, 4], [6, 7, 8, 9, 1, 2, 3, 4, 5], [7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 1, 2, 3, 4, 5, 6, 7], [9, 1, 2, 3, 4, 5, 6, 7, 8]]
trial = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

def done_or_not(board):
    t = np.array(board)
    t1 = t.transpose()
    fin = 0
    
    arr1 = np.arange(1, 10)
    arr2 = np.full((9, 9), arr1)

    triplet = t1.reshape(3, 3, 9)
    a, b, c = triplet[0], triplet[1], triplet[2]

    a = a.transpose().reshape(3, 3, 3)
    for i in a:
        k = np.sort(i.reshape(1, 9))
        if np.array_equal(k, [arr1]) == True: fin+=1 #fin = 3

    b = b.transpose().reshape(3, 3, 3)
    for i in b:
        k = np.sort(i.reshape(1, 9))
        if np.array_equal(k, [arr1]) == True: fin+=1 #fin = 6
        
    c = c.transpose().reshape(3, 3, 3)
    for i in c:
        k = np.sort(i.reshape(1, 9))
        if np.array_equal(k, [arr1]) == True: fin+=1 #fin = 9

    if (np.sort(t) == arr2).all() and (np.sort(t1) == arr2).all() == True and True: fin += 1 #fin = 10

    if fin == 10: print('Finished!')
    else: print('Try again!')
    
done_or_not(sudoku)
