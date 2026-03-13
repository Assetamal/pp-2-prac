a = int(input())
b = list(map(int , input().split()))
co = 0
for i in b:
    if i==0:
        continue
    else:
        co+=1
print(co)        