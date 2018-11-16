#CROP PLANNING - brute force
cost = [180,354.74,289.07]
price = [2.68,1.28,1.12]
# yield_ = [
#     [200,690,360], # 1
#     [178,450,380], # 2
#     [187,590,350], # 3
#     [150,510,375], # 4
#     [195,650,378], # 5
#     [205,420,310], # 6
#     [188,475,353], # 7
#     [179,550,290], # 8
#     [165,565,345], # 9
#     [180,635,365], # 10
#     [196,490,380], # 11
#     [191,560,370], # 12
#     [207,588,280], # 13
#     [130,598,320], # 14
#     [189,496,290], # 15
#     [197,640,325], # 16
#     [120,510,375], # 17
#     [195,488,360], # 18
#     [192,420,340], # 19
#     [180,665,330], # 20
#     [191,575,290], # 21
#     [204,570,387], # 22
#     [140,590,378], # 23
#     [172,545,365], # 24
#     [180,440,360], # 25
#     [141,531,368], # 26
#     [152,680,356], # 27
#     [181,555,295], # 28
#     [115,425,345], # 29
#     [190,580,315], # 30
#     [187,530,290], # 31
#     [175,575,360]  # 32
# ]
yield_ = [
    [100,345,180],
    [89,225,190],
    [93,295,175],
    [75,255,187],
    [97,325,189]
]
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
# s = [10000,20000,50000]
s = [1000,2000,5000]
# s = [2000,4000,10000]
# s = [3000,6000,15000]

M = 3
N = 5

MAX = 0
BEST_FITNESS = [0 for i in range(N)]
#initial value
x = [1 for i in range(N)]

def check_constraint(ele):
    if 1 in ele and 2 in ele and 3 in ele :
        check = True 
    else:
        return False
    for j in range(M):
        f = 0
        for i in range(N):
            Xij = 1 if j+1 == x[i] else 0
            f = f + (Xij*yield_[i][j]*area[i])
        f = (f-s[j])*price[j]
        if f < 0:
            return False
    return check

def combi(m,n):
    global MAX
    if(n >= N):
        # print(x, fitness(x))
        CURRENT_FITNESS = fitness(x)
        y = check_constraint(x)
        if MAX < CURRENT_FITNESS and y:
            MAX = CURRENT_FITNESS
            for index, item in enumerate(x):
                BEST_FITNESS[index] = item
        return 0
    for i in range(1,M+1):
        x[n] = i 
        combi(i,n+1)

def fitness(x = []):
    ans = 0
    for j in range(M):
        f = 0
        for i in range(N):
            Xij = 1 if j+1 == x[i] else 0
            f = f + (Xij*yield_[i][j]*area[i])
        f = (f-s[j])*price[j]
        sum_ = 0
        for i in range(N):
            Xij = 1 if j+1 == x[i] else 0
            sum_ = sum_ + (cost[j]*Xij*area[i])
        ans = ans+f-sum_
    return ans

#MAIN: 
import time
start = time.time()
combi(1,0)
print("BEST_SOLUTION = ",BEST_FITNESS)
print("MAX = ",MAX)

# show best solution
print("\nLand Number\tCrop")
for i in range(N):
    if(BEST_FITNESS[i]==1):
        print(str(i+1)+"\t\tCassava,")
    elif(BEST_FITNESS[i]==2):
        print(str(i+1)+"\t\tCorn,")
    elif(BEST_FITNESS[i]==3):
        print(str(i+1)+"\t\tRice,")
print("max profit : ",MAX)

end = time.time()
elapsed = end - start
print("Time = " , elapsed,"seconds")
end = time.time()
elapsed = end - start
print("Time = " , elapsed,"seconds")