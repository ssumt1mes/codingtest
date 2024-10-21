N,K = map(int,input().split())
list = []
for i in range(N) :
    list.append(int(input()))

count = 0
for i in range(len(list)) :
    pop = list.pop()
    if((K//pop)>=1) :
        count += K//pop
        K = K%pop

print(count)
