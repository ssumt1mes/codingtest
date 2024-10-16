import sys
N = int(sys.stdin.readline().rstrip())
list = []
for i in range(N) :
    k = int(sys.stdin.readline().rstrip())
    if(k==0) :
        if(len(list)==0) :
            continue
        else :
            list.pop()
    else :
        list.append(k)
sum = 0
for i in list :
    sum += i
print(sum)