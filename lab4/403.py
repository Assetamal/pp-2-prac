def div(s):
    for i in range(0 , s+1):
        if i % 12 == 0:
            yield i

s = int(input())
for j in div(s):
    print(j,end=" ")