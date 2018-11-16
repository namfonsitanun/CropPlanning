#test value
cost = [180,354.74,289.07]
price = [2.68,1.28,1.12]
yield_ = [
    [200,690,360], # 1
    [178,450,380], # 2
    [187,590,350], # 3
    [150,510,375], # 4
    [195,650,378], # 5
    [205,420,310], # 6
    [188,475,353], # 7
    [179,550,290], # 8
    [165,565,345], # 9
    [180,635,365], # 10
    [196,490,380], # 11
    [191,560,370], # 12
    [207,588,280], # 13
    [130,598,320], # 14
    [189,496,290], # 15
    [197,640,325], # 16
    [120,510,375], # 17
    [195,488,360], # 18
    [192,420,340], # 19
    [180,665,330], # 20
    [191,575,290], # 21
    [204,570,387], # 22
    [140,590,378], # 23
    [172,545,365], # 24
    [180,440,360], # 25
    [141,531,368], # 26
    [152,680,356], # 27
    [181,555,295], # 28
    [115,425,345], # 29
    [190,580,315], # 30
    [187,530,290], # 31
    [175,575,360]  # 32
]
# yield_ = [
#     [100,345,180],
#     [89,225,190],
#     [93,295,175],
#     [75,255,187],
#     [97,325,189]
# ]
# yield_ = [
#     [100,345,180],
#     [89,225,190],
#     [93,295,175],
#     [75,255,187],
#     [97,325,189],
#     [102,210,155],
#     [94,237,176],
#     [89,275,145],
#     [82,282,172],
#     [90,317,182]
# ]
# yield_ = [
#     [100,345,180],
#     [89,225,190],
#     [93,295,175],
#     [75,255,187],
#     [97,325,189],
#     [102,210,155],
#     [94,237,176],
#     [89,275,145],
#     [82,282,172],
#     [90,317,182],
#     [98,245,190],
#     [95,280,185],
#     [103,294,140],
#     [65,299,160],
#     [94,248,145]
# ]
area = [20000, 12000, 31000, 18760, 12940,
        13843, 23042, 8945, 28371, 5039, 
        18484, 19328, 11000, 9585, 4857, 
        28374, 19283, 19384, 12737, 18375, 
        7947, 9380, 20934, 8470, 22938, 
        28373, 10393, 19384, 10393, 29384, 
        19284, 9384]
#required quantities
s = [10000,20000,50000]
# s = [1000,2000,5000]
# s = [2000,4000,10000]
# s = [3000,6000,15000]
m = 3
n = 32

total = 1000
convergence = 100

bpop = False
maxFindTime = 0

maxFit = [0 for i in range(0,n)]
maxFit.append(0.0)

plotAverageX = []
plotAverageY = []
plotMaxX = []
plotMaxY = []

def check_constraint(ele):
    if 1 in ele and 2 in ele and 3 in ele :
        check = 0 
    else:
        return 1
    for j in range(m):
        f = 0
        for i in range(n):
            Xij = 1 if j+1 in ele else 0
            f = f + (Xij*yield_[i][j]*area[i])
        f = (f-s[j])
        if f < 0:
            return 1
    return check

def fitness(x = []):
    ans = 0
    for j in range(m):
        f = 0
        for i in range(n):
            Xij = 1 if x[i] == j+1 else 0
            f = f + (Xij*yield_[i][j]*area[i])
        f = (f-s[j])*price[j]
        sum_ = 0
        for i in range(n):
            Xij = 1 if x[i] == j+1 else 0
            sum_ = sum_ + (cost[j]*Xij*area[i])
        ans = ans + f - sum_
    return ans

def find_fitness():
    global x,bpop,total
    for index, fit in enumerate(x):
        if bpop and x[index][n] is not None:
            x[index].pop()
        x[index].append(fitness(fit))
    def getKey(item):
        return item[n]
    x = sorted(x, key = getKey, reverse=True)
    bpop = True
    while len(x) > total:
        temp = x.pop()
        # print(temp)

def inituniform():
    temp = []
    from random import randint
    for i in range(n):
        temp.append(randint(0,1))
    return temp

def initmutation():
    from random import randint
    temp1 = randint(1,convergence)
    temp2 = randint(0,n)
    temp3 = randint(0,total-1)
    return temp1,temp2,temp3

def checkmax():
    temp = x[0][n]
    for i in range((int)(total*0.1)):
        if temp != x[i][n]:
            return False
    return True
    
def crossoverfunction(fit1 = [], fit2 = []):
    global uniform
    for index, item in enumerate(uniform):
        fit1[index] = fit1[index] if item == 0 else fit2[index]
        fit2[index] = fit2[index] if item == 0 else fit1[index]

#main
import time
start = time.time()

uniform = inituniform()
print("UNIFORM = ",uniform)

mut_no,mut_pos,mut_dat = initmutation()
print("MUTATION AT GENERATION = ",mut_no)
print("MUTATION AT DATA = ",mut_dat)
print("MUTATION AT POSITION = ",mut_pos)

#generate 
x = []
from random import randint
for i in range(total):
    y = []
    while check_constraint(y):
        y = []
        for j in range(1,n+1):
            y.append(randint(1,3))
    x.append(y)
find_fitness()
# for i in range(0,total):
#     print(x[i])

# crossover
choose = (int)(total*0.5)
best = (int)(total*0.2)
for i in range(convergence):
    maxFindTime = 0
    uniform = inituniform();
    
    crossover = []
    for j in range(choose):
        crossover.append(x[j])
    fit1 = randint(1,best-1)
    fit2 = randint(1,choose-1)
    while crossover[fit1] == crossover[fit2] and maxFindTime < 50:
        fit1 = randint(1,best-1)
        fit2 = randint(1,choose-1)
        maxFindTime += 1
    
    crossoverfunction(crossover[fit1],crossover[fit2])
    while check_constraint(crossover[fit1]) or check_constraint(crossover[fit2]) and maxFindTime < 50:
        fit1 = randint(1,best-1)
        fit2 = randint(1,choose-1)
        maxFindTime += 1
        while crossover[fit1] == crossover[fit2] and maxFindTime < 50:
            fit1 = randint(1,best-1)
            fit2 = randint(1,choose-1)
            maxFindTime += 1
        crossoverfunction(crossover[fit1],crossover[fit2])

    x.append(crossover[fit1])
    x.append(crossover[fit2])

    #mutation
    if i == mut_no:
        z = randint(1,3)
        x[mut_dat][mut_pos] = z

    find_fitness()
    
    # keep max fitness from all generation
    for j in range(0,total):
        if not check_constraint(x[j]):
            if x[j][n] > maxFit[n] :
                import copy
                maxFit = copy.copy(x[j])
                break

    # data for plotting
    import numpy as np
    import itertools
    
    plotAverageX.append(i)
    plotMaxX.append(i)
    plotAverageY.append(sum(i[n] for i in x)/len(x))
    plotMaxY.append(maxFit[n])
    
    # check top 10 max similar
    if checkmax():
        break

# for element in x:
#     print (element)

print("BEST SOLUTION = ",maxFit)

# show best solution
print("\nLand Number\tCrop")
for i in range(n):
    if(maxFit[i]==1):
        print(str(i+1)+"\t\tCassava,")
    elif(maxFit[i]==2):
        print(str(i+1)+"\t\tCorn,")
    elif(maxFit[i]==3):
        print(str(i+1)+"\t\tRice,")
print("max profit : ",maxFit[n])

end = time.time()
elapsed = end - start
print("Time = " , elapsed,"seconds")

#plot graph
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
# PLOTX.insert(0,0)
# plotAverageY.insert(0,0)
ax.plot(plotAverageX, plotAverageY)
ax.plot(plotMaxX, plotMaxY)
# ax.plot([2],[150])

ax.set(xlabel='convergence (times)', ylabel='Fitness value',
       title='Genetric Algorithm Graph')
# ax.grid()

fig.savefig("test.png")
plt.show()