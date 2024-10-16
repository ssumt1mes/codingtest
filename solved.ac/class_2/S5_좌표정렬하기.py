N = int(input())
list_dot = []
for i in range(N) :
    list_dot.append(list(map(int,input().split())))

list_dot.sort()
for i in range(N) :
    print(list_dot[i][0],list_dot[i][1])
