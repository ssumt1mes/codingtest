import sys

#입력값을 받습니다 (각자 입력받는 방식을 다르게 했습니다.)
N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
T,P = map(int,sys.stdin.readline().split())
result = 0
#N_list 안에 있는 값을 비교해줍니다
for i in N_list :
    if(i%T==0) :
        result+=(i//T)
    else :
        result+=((i//T)+1)
print(result)
print(N//P,N%P)