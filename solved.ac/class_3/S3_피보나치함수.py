import sys
N = int(sys.stdin.readline().rstrip())
def fibonacci(n,zero_list,one_list) :
    if(n==0) :
        zero_list.append(0)
        return 0
    elif(n==1) :
        one_list.append(1)
        return 1
    else :
        return fibonacci(n-1,zero_list,one_list) + fibonacci(n-2,zero_list,one_list)
    
for i in range(N) :
    n = int(sys.stdin.readline().rstrip())
    zero_list = []
    one_list=  []
    fibonacci(n,zero_list,one_list)
    print(len(zero_list),len(one_list))
