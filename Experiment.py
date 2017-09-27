
# coding: utf-8

# In[1]:

from sudoku import sudoku,clue_plus_one
import time
import pickle
import csv


# In[2]:

N = 100


# In[3]:

clues17 = [list(map(int,list(line.strip()))) for line in open('raw_17_clue_sudokus.txt')]
with open('clues-17.pickle','wb') as clues_file:
    pickle.dump(clues17,clues_file)


# In[4]:

clues18 = []
i = 0
for clue in clues17[:N]:
    clues18.append(clue_plus_one(clue))
    i+=1
    print(i)
with open('clues-18.pickle','wb') as clues_file:
    pickle.dump(clues18,clues_file)


# In[5]:

with open('clues-17.pickle','rb') as clues_file:
    clues17 = pickle.load(clues_file)
with open('clues-18.pickle','rb') as clues_file:
    clues18 = pickle.load(clues_file)


# In[6]:

result_dict = {'clue17':[],'clue18':[]}
# ,'clue17-':[],'clue18-':[]
csv_dict = {key:[] for key in ['clue17']+list(range(1,65))}
# csv_dict1 = {key:[] for key in ['clue17']+list(range(1,65))}


# In[ ]:

for i in range(N):
    with open('result'+str(i+1)+'.txt','w') as result:
        startTime = time.process_time()
        a = sudoku(clues17[i])
        endTime = time.process_time()
        costTime = endTime - startTime
#         startTime1 = time.process_time()
#         b = sudoku(clues17[i],True)
#         endTime1 = time.process_time()
#         costTime1 = endTime1 - startTime1
        result.write(str(costTime)+'\n')
        result_dict['clue17'].append(costTime)
#         result_dict['clue17-'].append(costTime1)
        csv_dict['clue17'].append(costTime)
#         csv_dict1['clue17'].append(costTime1)
        result_list = []
#         result_list1 = []
        for j in range(len(clues18[i])):
            startTime = time.process_time()
            a = sudoku(clues18[i][j])
            endTime = time.process_time()
            costTime = endTime - startTime
#             startTime1 = time.process_time()
#             b = sudoku(clues17[i],True)
#             endTime1 = time.process_time()
#             costTime1 = endTime1 - startTime1
            result.write(str(costTime)+'\n')
            result_list.append(costTime)
#             result_list1.append(costTime1)
            csv_dict[j+1].append(costTime)
#             csv_dict1[j+1].append(costTime1)
    result_dict['clue18'].append(result_list)
#     result_dict['clue18-'].append(result_list1)
    print(i+1)


# In[ ]:

with open('csv_dict.pickle','wb') as csv_file:
    pickle.dump(csv_dict,csv_file)
with open('csv_dict1.pickle','wb') as csv_file:
    pickle.dump(csv_dict1,csv_file)
with open('result_dict.pickle','wb') as result_file:
    pickle.dump(result_dict,result_file)

