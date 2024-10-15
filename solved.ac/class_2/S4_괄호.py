import sys

N = int(input())

for i in range(N) :
    N_list = list(sys.stdin.readline().rstrip())
    check_list = []
    answer = ''
    for i in N_list :
        if(i=='(') :
            check_list.append(check_list)
        else :
            if(len(check_list)!=0) :
                check_list.pop(-1)
            else :
                answer = 'NO'
                break
    if(len(check_list)==0 and answer=='') :
        answer = 'YES'
    else :
        answer = 'NO'
    print(answer)
    

