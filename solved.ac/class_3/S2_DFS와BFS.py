import sys
N,M,V = map(int,sys.stdin.readline().split())
list_dot=[]
for i in range(M) :
    list_dot.append(list(map(int,sys.stdin.readline().split())))
list_dot.sort()

def DFS(V, list_dot) :
    visited = [V]
    index = 0
    while(len(visited)!=N) :
        if(V==list_dot[index][0] & (V not in visited)) :
            visited.append(list_dot[index][1])
            index= 0
            V = list_dot[index][1]
        elif(V==list_dot[index][1] & (V not in visited)) :
            visited.append(list_dot[index][0])
            index=0
            V = list_dot[index][0]
        else :
            index+=1
    print(visited)
    return visited

def BFS(V,list_dot) :
    visited = [V]


print(DFS(V, list_dot),BFS(V,list_dot))