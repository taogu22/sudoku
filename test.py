from sudoku import sudokuSol
import time

file = open("raw_17_clue_sudokus.txt")
# read the first 81 characters;

result = open('result_1.txt', 'w')

N = 20
for i in range(N):
        # import each line in "raw_17_clue_sudokus.txt" withouout '\n';
        line = (file.readline()).rstrip('\n')
        # here we turn every sting into a list, and represent a sudoku by a list;
        puz = list(map(int, list(line))) 
        startTime = time.process_time()
        print(sudokuSol(puz))
        endTime = time.process_time()
        # the running time for the current puzzel is endTime - startTime;
        costTime = endTime - startTime
        print("Runing time is {}".format(costTime))
        # write the running time in 'result.txt';
        result.write(str(costTime) + '\n')    

result.close()
