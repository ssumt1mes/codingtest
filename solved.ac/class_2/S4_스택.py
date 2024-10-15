import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N) :
    com_list = list(sys.stdin.readline().split())
    if(len(com_list)>1) :
        stack.append(com_list[1])
    else :
        if(com_list[0]=='top') :
            if(len(stack)==0) :
                print(-1)
            else :
                print(stack[-1])
        elif(com_list[0]=='size') :
            print(len(stack))
        elif(com_list[0]=='pop') :
            if(len(stack)==0) :
                print(-1)
            else :
                print(stack.pop(-1))
        elif(com_list[0]=='empty') :
            if(len(stack)==0) :
                print(1)
            else :
                print(0)
        

