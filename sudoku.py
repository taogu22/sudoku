def sudoku(clue):
### INPUT:
##### clue = list. Contains all the sudoku clues. Unknown information is denoted by 0.
##### n = number. The size of sudoku.
##### Elimination = True/False. When True: Delete impossible clauses before doing pycosat.
### OUTPUT:
##### A list of numbers, in the form "grid number*10+solution".
### SET PARAMETERS
    import numpy as np
    import itertools
    import pycosat
    x = range(1,82)
    n = range(1,10)
    matrix = np.array(x)
    matrix_n = np.array(n)
       # a list of all the grid numbers, from 1 to 81
    pre = [[(i+1)*10+int(clue[i])] for i in range(len(clue)) if clue[i]!=0]
       # convert the clue from list to the form used in pycolist
### RULE1: 1-9 ALL IN EACH BLOCK/ROW/COLUMN
    matrix = matrix.reshape(9,9)
    condition_matrix = np.vstack((matrix,matrix.transpose(),matrix.reshape(3,3,3,3).transpose(0, 2, 1, 3).reshape(9,9))).repeat(9,axis=0)
        # put all the rows & columns & blocks into condition matrix
    a = np.tile(matrix_n,27).reshape(243,-1)
        # for each possible solution, it is: in grid1 or in grid2 or in grid3 ...or in grid 9.
    rule1 = (condition_matrix*10+a).tolist()
### RULE2: ONLY 1 NUMBER IN EACH GRID
    rule2 = []
    grid_matrix = matrix.reshape(81,-1).repeat(9,axis=1)*10 + matrix_n
    # in this form: [[11, 12, 13, 14, 15, 16, 17, 18, 19],[21, 22, 23, 24, 25, 26, 27, 28, 29],...]
     # an element in this list indicates the possiblities one gird may have
    for gridcondition in grid_matrix:
        rule2.extend([[-int(grid[0]),-int(grid[1])] for grid in itertools.combinations(gridcondition,2)])
        # transform "11->(-12 and -13 and -14 ... and -19)" into "(-11 or -12) and (-11 or -13) and ... and (-11 or -19)"
### CALCULATE SOLUTIONS
        result = pycosat.solve(pre+rule1+rule2)
    if type(result) != str:
        solution = [sol for sol in pycosat.solve(pre+rule1+rule2) if sol>0]
        # delete all the unrelated answers, so the list only contains the answer for the 81 grids
    else:
        solution = result
        # for the case that there is no answer
    return solution

def clue_plus_one(clue):
    import numpy as np
    clues = []
    solution = list(map(lambda x:int(str(x)[-1]),sudoku(clue)))
    for i in range(len(solution)):
        if clue[i]==0:
            c = np.array(clue)
            c[i] = solution[i]
            clues.append(c.tolist())
    return clues

def clue_plus_n(clue12,solution123,cob_list):
    import itertools
    import numpy as np
    clues = []
    for cob in cob_list:
        flag = 0
        for ccc in cob:
            if clue12[ccc]!=0:
                flag = 1
                break
        if flag == 0:
            A1 = np.array(clue12)
            for ccc in cob:
                A1[ccc]=solution123[ccc]
            clues.append(A1.tolist())
        if len(clues)==10:
            break
    return clues
