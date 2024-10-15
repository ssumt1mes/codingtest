import sys

N = int(sys.stdin.readline())
N_list = list(map(float,sys.stdin.readline().split()))

max_N = max(N_list)
sum = 0
for i in range(len(N_list)) :
    sum+= N_list[i]/max_N*100

averages = 0
averages = sum / len(N_list)
print(averages)