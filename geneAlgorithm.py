import numpy as np 
from random import *
import copy
import time

humanNum = 10
geneNum = 10
chromosome = [[randint(0,1) for m in range(geneNum)] for n in range(humanNum)]
superiority = [0] * humanNum
sortSuperiority = [0] * humanNum
topHumanIndex = [0] * 5
topFiveList = [[0 for m in range(10)] for n in range(5)]

def find_index(data, target):
  res = []
  lis = data
  while True:
    try:
      res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0))
      lis = data[res[-1]+1:]
    except:
      break     
  return res

while(1):
    for i in range(humanNum): 
        superiority[i] = sum(chromosome[i][0:geneNum])

    noneSortSuperiority = superiority[0:10]
    superiority.sort(reverse=True)
    sortSuperiority = superiority[0:10]

    z = 0
    while z != 5:
        index = find_index(noneSortSuperiority, sortSuperiority[z])
        if len(index) > 1:
            for i in range(len(index)):
                topHumanIndex[z] = index[i]
                z = z+1
                if z == 5:
                    break
        else:
            topHumanIndex[z] = index[0]
            z = z+1
            if z == 5:
                break
    for i in range(5):
        topFiveList[i][0:10] = chromosome[topHumanIndex[i]][0:10]

    for i in range(5,10):
           for m in range(10):
                chromosome[i][m] = randint(0,1)
    
    for i in range(5):
        chromosome[i][0:5] = topFiveList[randint(0,4)][0:5]
        chromosome[i][5:10] = topFiveList[randint(0,4)][5:10]

    for i in range(10):
        print(chromosome[i][0:10])
    
    print('------------------------------------')
    time.sleep(0.3)

    #유전알고리즘 수정하기 집가서 !! 가장 수치가 높은 값은 