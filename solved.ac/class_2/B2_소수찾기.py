import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
result = 0
for i in N_list :
    for j in range(2,i+1) :
        if (i%j)==0 :
            if i == j :
                result +=1
            break
print(result) 
