computer = int(input())
connected_computer = int(input())
connect_list = [[] for _ in range(100)]
bool_list = [False for _ in range(100)]
for i in range(connected_computer) :
    lists = (list(map(int,input().split())))
    connect_list[lists[0]].append(lists[1])
    connect_list[lists[1]].append(lists[0])


check_list = connect_list[1]
bool_list[1] = True

while(1) :
    count = 0
    for i in check_list :
        if(bool_list[i]==True) :
            count+=1
    if(count==len(check_list)) :
        break
    for i in check_list :
        for j in connect_list[i] :
            if j == 0 :
                continue
            if(bool_list[j]==False) :
                check_list.append(j)
                bool_list[j] = True
check_list = set(check_list)
print(len(check_list))

    
